import pymongo
from pymongo import MongoClient
'''cluster = MongoClient(
    "mongodb+srv://anoop31:anoop31@cluster0-mpnrr.azure.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["sample_airbnb"]
collection = db["listingsAndReviews"]
result = collection.find({"_id": "10006546"})
for result in result:
    print(result)

print("Hello world")'''
cluster = MongoClient(
    "mongodb+srv://anoop31:anoop31@cluster0-mpnrr.azure.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["sample_airbnb"]
collection = db["listingsAndReviews"]
results = collection.find({"_id": "10006546"})
#results = collection.find({id: t1})
for result in results:
    print(result["listing_url"])
    x = result["listing_url"]
    d = {"listing_url": x}
    print(d)
