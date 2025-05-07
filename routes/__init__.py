# routes/__init__.py
def register_routes(app):
    """
    Mendaftarkan semua route ke aplikasi Flask.
    
    Args:
        app: Aplikasi Flask
    """
    from routes.main import main_bp
    app.register_blueprint(main_bp)
