import psycopg2
from helper import *

conn = connect_to_db()
cur = conn.cursor()

# SQL commands to execute
create_schema = """
CREATE SCHEMA IF NOT EXISTS test_schema;
"""

create_table = """
CREATE TABLE test_schema.init_test_table_2 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20)
);
"""

# Execute the commands
try:
    cur.execute(create_schema)
    cur.execute(create_table)
    conn.commit()  # Commit the changes to the database
    print("Table created successfully!")
except psycopg2.Error as e:
    print(f"Error creating table: {e}")
    conn.rollback()  # Rollback in case of an error

# Close the connection
cur.close()
conn.close()