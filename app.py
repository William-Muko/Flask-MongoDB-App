from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client["mydatabase"]

@app.route("/")
def home():
    return "Hello from Flask with MongoDB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
