# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:50:52 2020

@author: Anoop
"""
import mongodb
from flask import Flask, request, json, jsonify
import config

app = Flask(__name__)


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


'''@app.route('/login/<username>', methods=['GET'])
def login(username):
    print(username)'''
# //concept of Post and Get


@app.route('/getreviewbyid/<id>', methods=['GET', 'OPTIONS'])
def getreviewbyid(id):
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_prelight_response()
    elif request.method == "GET":  # The actual request following the preflight
        collection = mongodb.database()  # collection
        document = collection.find_one({"_id": id})
        return _corsify_actual_response(jsonify(document))
    #collection=mongodb.database() # collection
    #document=collection.find_one({"_id":id})
    #return jsonify(document)


@app.route('/getreviews', methods=['GET'])
def getreviews():
    collection = mongodb.database()  # collection
    documents = list(collection.find())
    return jsonify(documents)


@app.route('/insert_airbnb', methods=['POST', 'OPTIONS'])
def insert_airbnb():
    review = request.json
    print("Inserting review:", review)
    collection = mongodb.database()
    addeddocument = collection.insert_one(review)
    print("Document added sucessfully:", addeddocument)
    return True


@app.route('/update_airbnb', methods=['POST', 'OPTIONS'])
def update_airbnb():
    reqData = request.json
    k2 = config.id
    v2 = reqData[k2]
    k3 = config.name
    v3 = reqData[k3]
    #input_id=1245156
    #upd_value="Anoop charming pentahouse"
    #print(upd_value)
    conn = mongodb.database()
    rec_id2 = conn.update_one(
        {k2: v2}, {"$set": {k3: v3}})
    print("Data updated with id", rec_id2)
    return config.update


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)


#z=update_airbnb()
#x = data_airbnb()
#print(x)

#y=insert_airbnb()

