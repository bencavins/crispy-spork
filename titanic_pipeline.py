import pandas as pd
from pipeline import connect_to_pg, execute_ddl
import queries
import psycopg2


def get_titanic_data(filename='titanic.csv'):
    df = pd.read_csv(filename)
    return df


def insert_titanic_data(titanic_df):
    for row in titanic_df:
        insert_statement = f"""
        INSERT INTO titanic
        (survived, pclass, name, sex, sibs_spouses, parents_children, fare)
        VALUES
        ({row['Survived']},{},{},{},{},{},{})
        """
        execute_ddl(insert_statement)


if __name__ == '__main__':
    titanic_data = get_titanic_data()
    pg_conn = connect_to_pg()
    execute_ddl(pg_conn, queries.create_titanic_table)
    insert_titanic_data(titanic_data)
    pg_conn.commit()