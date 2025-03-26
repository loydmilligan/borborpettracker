from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)
    
    # Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bilbo_pet_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database with the app
    db.init_app(app)
    
    # Import and register blueprints here later
    
    return app