import psycopg2
from db_scripts.helper import *

def insert_journal_entry(entry_type, entry):
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        # Use parameterized query to safely handle single quotes
        insert_query = """
        INSERT INTO test_schema.journal_entries (entry_type, entry, user_id)
        VALUES (%s, %s, %s)
        """

        # Pass values as a tuple
        values = (entry_type, entry, 0)
        cur.execute(insert_query, values)

        conn.commit()
        print("Updated entry successfully")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        conn.rollback() 
    finally:
        cur.close()
        conn.close()
