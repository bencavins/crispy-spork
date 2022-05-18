import psycopg2
import sqlite3
import queries


dbname = 'wuztkssx'
user = 'wuztkssx'
password = ''
hostname = 'drona.db.elephantsql.com'


def connect_to_pg():
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=hostname
    )
    return connection


def connect_to_sqlite(db_name='rpg_db.sqlite3'):
    """Connect to a SQLite database"""
    return sqlite3.connect(db_name)


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def execute_ddl(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)


def insert_rpg_data(connection, rpg_data):
    tuple_strs = ','.join([str(row) for row in rpg_data])
    insert_statement = f"""
    INSERT INTO charactercreator_character
    (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES
    {tuple_strs}
    """
    execute_ddl(connection, insert_statement)



if __name__ == "__main__":
    sqlite_conn = connect_to_sqlite()
    rpg_data = execute_query(sqlite_conn, queries.select_all)
    pg_conn = connect_to_pg()
    execute_ddl(pg_conn, queries.create_character_table)
    insert_rpg_data(pg_conn, rpg_data)
    pg_conn.commit()
