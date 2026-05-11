from flask import Flask

from .extensions import appbuilder, db



def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)        # añadido para inicializar la extensión de SQLAlchemy
    with app.app_context():
        from .models import Categoria, Producto  # Importar los modelos para que SQLAlchemy los reconozca
        db.create_all()
        appbuilder.init_app(app, db. session)  # añadido para inicializar AppBuilder con la sesión de SQLAlchemy            
        from . import views  # Importar las vistas para que se registren en AppBuilder
        
        # Registering the views and APIs
        ...
    return app
