from flask import Flask
from dotenv import dotenv_values
from pprint import pprint
from flask_pymongo import PyMongo
config = dotenv_values(".env")

app = Flask(__name__)
app.config["MONGO_URI"] = config['MONGO_URI']
mongo = PyMongo(app)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)