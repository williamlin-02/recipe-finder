from flask import Flask
from flask_pymongo import PyMongo
from dotenv import dotenv_values
from pprint import pprint
from pymongo import MongoClient
config = dotenv_values(".env")


MONGO_URI = config['MONGO_URI']
app = Flask(__name__)
client = MongoClient(MONGO_URI, connect=False)
db=client.admin
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)