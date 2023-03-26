import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ep1-c"]
collection = db["parcial1"]


