import pymongo
from db import connect_to_db, execute_query
import queries
from pprint import pprint


def create_mdb_conn():
    client = pymongo.MongoClient(
        "mongodb+srv://bencavins1:@cluster0.2vdvn.mongodb.net/?retryWrites=true&w=majority",
        )
    db = client.test
    return db


def tuples_to_dicts(rpg_data):
    result = []
    for row in rpg_data:
        query = f"""
        SELECT name, value, weight
        FROM charactercreator_character_inventory as ci
        JOIN armory_item as ai 
            ON ci.item_id = ai.item_id
        WHERE ci.character_id = {row[0]}
        """
        sqlite_conn = connect_to_db()
        item_data = execute_query(sqlite_conn, query)
        items = []
        for item_row in item_data:
            item_dict = {
                'name': item_row[0],
                'value': item_row[1],
                'weight': item_row[2],
            }
            items.append(item_dict)
        d = {
            'character_id': row[0],
            'name': row[1],
            'level': row[2],
            'exp': row[3],
            'hp': row[4],
            'strength': row[5],
            'intelligence': row[6],
            'dexterity': row[7],
            'wisdom': row[8],
            'items': items,
        }
        result.append(d)
    return result


if __name__ == '__main__':
    sqlite_conn = connect_to_db()
    rpg_data = execute_query(sqlite_conn, queries.select_all)
    rpg_dicts = tuples_to_dicts(rpg_data)
    db = create_mdb_conn()
    db.character.insert_many(rpg_dicts)

    # db.character.delete_many({})


# db.person.insert_one({'junk': 'whatever'})
# db.person.delete_one({'age': 36})
# db.person.insert_many([{},{}])
# cursor = db.person.find({'age': 36})
# print(list(cursor))



