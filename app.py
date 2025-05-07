# app.py
from flask import Flask
from routes import register_routes
from config import Config

def create_app(config_class=Config):
    """Fungsi factory untuk membuat aplikasi Flask."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Mendaftarkan route
    register_routes(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)