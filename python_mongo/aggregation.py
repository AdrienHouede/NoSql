from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

pipeline = [
    {"$match": {"age": {"$gt": 25}}},
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]

results = collection.aggregate(pipeline)

for result in results:
    print(result)