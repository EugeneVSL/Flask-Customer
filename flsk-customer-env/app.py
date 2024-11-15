from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/status", methods=['GET'])
def status():
    return "<p>OK</p>"

@app.route("/customer/<id>", methods=['GET'])
def show_customer_profile(id: int):
    pass