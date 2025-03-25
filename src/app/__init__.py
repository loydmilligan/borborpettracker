from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
db = SQLAlchemy()

def create_app():
    """
    Create and configure the Flask application instance.
    Returns a configured Flask app with initialized extensions.
    """
    app = Flask(__name__)
    
    # Basic configuration (to be expanded in config module)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bilbo_pet_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    db.init_app(app)
    
    return app