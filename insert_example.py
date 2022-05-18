import sqlite3

conn = sqlite3.connect('mock_db.sqlite3')
cursor = conn.cursor()

create_statement = """
CREATE TABLE test_table
(id INTEGER PRIMARY KEY,
name VARCHAR(36),
age INTEGER);
"""

# cursor.execute(create_statement)

insert_statement = """
INSERT INTO test_table (name, age)
VALUES
("betty", 24),
("rob", 55)
"""
cursor.execute(insert_statement)
conn.commit()
cursor.close()