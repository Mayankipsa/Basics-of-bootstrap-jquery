# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:42:33 2020

@author: Anoop
"""

import pymongo
from pymongo import MongoClient


def database():  # Get collection
    cluster = MongoClient(
        "mongodb+srv://anoop31:anoop31@cluster0-mpnrr.azure.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = cluster["sample_airbnb"]
    collection = db["listingsAndReviews"]
    return collection
