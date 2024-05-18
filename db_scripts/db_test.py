import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


# Load environment variables
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')   # Default to 'localhost' if not provided
DB_PORT = os.environ.get('DB_PORT')       # Default to standard PostgreSQL port

# Establish connection using environment variables
try:
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
except psycopg2.OperationalError as e:
    print(f"Unable to connect: {e}")
    exit(1) 

cur = conn.cursor()

# SQL commands to execute
create_schema = """
CREATE SCHEMA IF NOT EXISTS test_schema;
"""

create_table = """
CREATE TABLE test_schema.init_test_table_1 (
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