# config.py
import os

class Config:
    """Konfigurasi dasar aplikasi."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    MODEL_PATH = os.environ.get('MODEL_PATH') or 'models/saved_model'