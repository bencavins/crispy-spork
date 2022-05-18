import sqlite3
import queries

def connect_to_db(db_name='rpg_db.sqlite3'):
    """Connect to a database"""
    return sqlite3.connect(db_name)

def execute_query(connection, query):
    """Execture query using given connection"""
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == '__main__':
    connection = connect_to_db()
    results = execute_query(connection, queries.select_all)
    print(results)