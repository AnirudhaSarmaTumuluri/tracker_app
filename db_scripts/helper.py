import psycopg2
import os
from dotenv import load_dotenv
 

def connect_to_db():
    load_dotenv()
    
    # Load environment variables
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST') 
    DB_PORT = os.environ.get('DB_PORT')   
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Unable to connect: {e}")
        return None