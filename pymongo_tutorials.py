from pymongo import MongoClient
import datetime

# connect to a collection
client = MongoClient()
db = client.test_database
collection = db.test_collection

# insert a document in a collection
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow(),
}
collection.insert_one(post)

# list/find documents from a collection
print(db.list_collection_names())
print(collection.find_one())
print(collection.find_one({"author": "Mike"}))
print([x for x in collection.find()])

# delete a document from a collection
collection.delete_one({"author": "Mike"})
