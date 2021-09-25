from pymongo import MongoClient

# connect to a collection & fetch docs count
client = MongoClient()
db = client.test_database
count = db.test_collection.count()
print(count)
