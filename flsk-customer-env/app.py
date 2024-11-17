import sqlite3
import json
from flask import Flask 
from db.connection import DBConnection

# JWT modules
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

@app.route("/status", methods=["GET"])
def status():
    return "<p>OK</p>"

@app.route("/customer/<int:id>", methods=["GET"])
def show_customer_profile(id):

    # establish the db connection 
    db = DBConnection()
    conn = db.get_db().cursor()
    
    # get the customer
    data = conn.execute(f"""SELECT * from Customer WHERE CustomerId = {id}""")
    customer = data.fetchone()

    # close the db connection 
    db.close_connection(conn)

    # format the output
    response = {
        "id": customer[0],
        "first_name": customer[1],
        "last_name": customer[2],
        "company": customer[3],
        "address": customer[4],
        "city": customer[5],
        "state": customer[6],
        "country": customer[7],
        "postal_code": customer[8],
        "phone": customer[9],
    }

    # return as JSON
    return json.dumps(response)

if __name__ == "__main__": 
    app.run(debug=True) 