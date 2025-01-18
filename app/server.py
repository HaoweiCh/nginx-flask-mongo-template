#!/usr/bin/env python
import os

import flask
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:27017")


@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return flask.jsonify({'err': "Server not available", "code": 503})
    return flask.jsonify(dict(msg="Hello from the MongoDB client!", code=200)), 200  # 返回 200 状态码


@app.route("/health")
def health():
    return flask.jsonify(dict(msg="ok", code=200)), 200  # 返回 200 状态码


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
