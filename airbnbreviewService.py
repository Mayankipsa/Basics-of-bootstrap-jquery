# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:50:52 2020

@author: Anoop
"""
import mongodb
from flask import Flask, request, json, jsonify,render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'CONTENT-TYPE'
cors = CORS(app, resources={
            r"/api/*": {"origins": "localhost"}}, headers="Content-Type")



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
    


@app.route('/getreviews', methods=['GET'])
def getreviews():
    collection = mongodb.database()  # collection
    documents = list(collection.find())
    return jsonify(documents)




@app.route('/insert_airbnb', methods=['POST', 'OPTIONS'])
@cross_origin(allow_headers=['Content-Type'])
def insert_airbnb():
    '''if request.method == "OPTIONS":  # CORS preflight
            return _build_cors_prelight_response()
    elif request.method == "POST":  # The actual request following the preflight'''
    review = request.json
    print("Inserting review:", review)
    collection = mongodb.database()
    addeddocument = collection.insert_one(review)
    print("Document added sucessfully:", addeddocument)
    #status={"status":"Record added sucessfully"}
    return 

@app.route('/update_airbnb', methods=['POST', 'OPTIONS'])
@cross_origin(allow_headers=['Content-Type'])
def update_airbnb():
    updatereview = request.json
    #cvtdct = json.loads(updatereview)
    print(updatereview)
    updatereview1 = {"$set": updatereview}
    #updatereview1 = {"$set": {"_id": "1", "bed_type": "2", "listing_url": "2"}}
    #print(updatereview1)
    y=updatereview["_id"]
    print(y)
    query = {"_id":y }
    #print(query)
    print("Updated Review:", updatereview)
    collection = mongodb.database()
    updatereview = collection.update_one(query, updatereview1)
    #print("Data updated with id", updatereview)
    return 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)


#z=update_airbnb()
#x = data_airbnb()
#print(x)

#y=insert_airbnb()

