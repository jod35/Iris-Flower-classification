from flask import Flask
from main.app.classify.routes import app_blueprint


def create_app():
    app=Flask(__name__)

    app.register_blueprint(app_blueprint)
    app.secret_key="iamsecret"

    return app