from flask import Flask

from .extensions import appbuilder, db
from .extensions import appbuilder


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)        # añadido para inicializar la extensión de SQLAlchemy
    with app.app_context():
        appbuilder.init_app(app, db. session)  # añadido para inicializar AppBuilder con la sesión de SQLAlchemy    
        db.create_all()
        # Registering the views and APIs
        ...
    return app
