import sqlite3
import json
from flask import Flask, jsonify, request
from markupsafe import escape
from db.connection import DBConnection


app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    return "<p>OK</p>"

@app.route("/customer/<int:id>", methods=["GET"])
def show_customer_profile(id):

    # establish the db connection 
    db = DBConnection()
    conn = db.get_db().cursor()
    
    # get the customer
    data = conn.execute(f"SELECT CustomerId, FirstName from Customer WHERE CustomerId = {id}")
    customer = data.fetchone()

    # close the db connection 
    db.close_connection(conn)

    # format the output
    response = {
        "id": customer[0],
        "first_name": customer[1]
    }

    # return as JSON
    return json.dumps(response)

if __name__ == "__main__": 
    app.run(debug=True) 