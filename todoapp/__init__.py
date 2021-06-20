from flask import Flask

from .extensions import mongo


def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://djviodes:84D3LTN3JBpuyFwe@cluster0.lvdcd.mongodb.net/myDb?retryWrites=true&w=majority'

    mongo.init_app(app)

    return app
