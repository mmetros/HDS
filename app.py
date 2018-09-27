from flask import Flask, render_template, request, jsonify
from flask_restful import Api
import sqlite3
from manufacturer import Manufacturer, Manufacturers
from home import Home


app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(Manufacturer, '/manufacturers/<string:name>', '/admin')
api.add_resource(Manufacturers, '/manufacturers')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
