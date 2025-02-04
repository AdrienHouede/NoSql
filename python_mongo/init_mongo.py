from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35},
    {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)

query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

query = {"age": {"$gt": 25}}
projection = {"_id": 0, "name": 1, "email": 1}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)