import sqlite3
import os

def create_database(db_path, schema_path):
    """
    Create SQLite database by executing schema.sql
    :param db_path: Path to the SQLite database file
    :param schema_path: Path to the SQL schema file
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to the database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    
    # Read the schema file
    with open(schema_path, 'r') as schema_file:
        schema_sql = schema_file.read()
    
    # Execute the schema
    conn.executescript(schema_sql)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Paths relative to the script location
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, 'bilbo_pet_tracker.db')
    SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')
    
    create_database(DB_PATH, SCHEMA_PATH)
