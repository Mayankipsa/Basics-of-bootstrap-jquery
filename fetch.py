import pymongo
from pymongo import MongoClient
from flask import Flask, request, json,jsonify
from flask import make_response, current_app
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'CONTENT-TYPE'
cors = CORS(app, resources={r"/api/*": {"origins": "localhost"}}, headers="Content-Type")


# Use-case1 Scenario 1
@app.route('/fetchData_airbnb', methods=['POST', 'OPTIONS'])
@cross_origin(allow_headers=['Content-Type'])
def data_airbnb():
    reqData = request.json
    print(reqData)
    id="_id"
    print(id)
    t1=reqData[id]
    print(t1)
    cluster = MongoClient(
        "mongodb+srv://anoop31:anoop31@cluster0-mpnrr.azure.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = cluster["sample_airbnb"]
    collection = db["listingsAndReviews"]
    results = collection.find({"_id":"10006546"})
    #results = collection.find({"id":"t1"})
    for result in results:
        print(result["listing_url"])
        x = result["listing_url"]
        d = {"listing_url":x}
        print(d)
    return jsonify(d)

if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0', port=9090)
