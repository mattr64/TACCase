from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['networksdb']
devices_collection = db['devices']

# Retrieve all documents in the collection
documents = devices_collection.find()

# Print each document
for document in documents:
    print(document)

# Close the MongoDB connection
client.close()
