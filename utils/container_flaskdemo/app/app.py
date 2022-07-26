# flask_web/app.py
import os
from flask import jsonify
from flask import Flask, abort, session, request, redirect

app = Flask(__name__)

@app.route("/")
def health() :
    # """health route"""
    print("'Hey, we have Flask in a Docker container!'")
    state = {"status": "Hey, we have Flask in a Docker container!"}
    return jsonify(state)

if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0')