import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://anoop31:anoop31@cluster0-spyat.azure.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["sample_airbnb"]
collection=db["listingsAndReviews"]
result=collection.find({"_id":"10006546"})
for result in result:
    print(result["_id"])

print("Hello world")
