import os
import sys

# Print current working directory and Python path for debugging
print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

# Add the project root and src directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
sys.path.insert(0, src_dir)

# Debugging import
try:
    from app.models import Base
    print("Successfully imported Base from app.models")
except ImportError as e:
    print(f"Import Error: {e}")
    # List contents of potential import directories
    print("Contents of current directory:", os.listdir('.'))
    print("Contents of src directory:", os.listdir(src_dir))
    print("Contents of app directory:", os.listdir(os.path.join(src_dir, 'app')))
    raise

from sqlalchemy import create_engine

def create_database(db_path):
    """
    Create SQLite database using SQLAlchemy models
    :param db_path: Path to the SQLite database file
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Create SQLAlchemy engine
    engine = create_engine(f'sqlite:///{db_path}')
    
    # Create all tables defined in the models
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    # Paths relative to the script location
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, 'bilbo_pet_tracker.db')
    
    create_database(DB_PATH)