from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import get_jwt, jwt_required
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_
import schemas
import models
from passlib.hash import pbkdf2_sha256
from database import db

blp = Blueprint("users", __name__, "User related endpoints")


@blp.route("/users")
class Users(MethodView):
    def get(self):
        return {"msg": "ok"}


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(schemas.UserSchema)
    @blp.response(200, schemas.DisplayUserSchema)
    def post(self, user_data):
        if models.User.query.filter(
            or_(
                models.User.username == user_data["username"],
                models.User.email == user_data["email"],
            )
        ).first():
            abort(409)
        user = models.User(
            username=user_data["username"],
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()
        return {"msg": "success", "response": user}


@blp.route("/login")
class UserLogin(MethodView):
    def post(self):
        return {}


@blp.route("/logout")
class UserLogout(MethodView):
    def post(self):
        return {}


@blp.route("/user/<int:id>")
class User(MethodView):
    def get(self):
        return {}
