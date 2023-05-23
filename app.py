from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_smorest import Api
import routes
from database.db import db
from flask_jwt_extended import create_access_token, JWTManager
from models.user import User

load_dotenv()


def create_app():
    app = Flask(__name__)
    # autodocs config
    app.config["API_TITLE"] = "Music App"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # database config
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}/{environ.get('DB_NAME')}"
    db.init_app(app)

    # jwt config
    app.config["JWT_SECRET_KEY"] = f"{environ.get('JWT_SECRET_KEY')}"
    jwt = JWTManager(app)

    api = Api(app)

    # register blueprints
    api.register_blueprint(routes.UserBlueprint)

    with app.app_context():
        db.create_all()

    app.run()

    return app


if __name__ == "__main__":
    create_app()
