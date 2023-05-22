from flask import Flask
from dotenv import load_dotenv
from os import environ

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.run()


if __name__ == "__main__":
    create_app()
