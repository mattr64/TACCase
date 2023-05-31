from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['networksdb']
devices_collection = db['devices']

# Test data
test_data = [
    {
        'hostname': 'router01',
        'device_type': 'Router',
        'serial': '1234567890',
        'product_id': 'PRODUCT_ID_1'
    },
    {
        'hostname': 'switch01',
        'device_type': 'Switch',
        'serial': '0987654321',
        'product_id': 'PRODUCT_ID_2'
    },
    # Add more test data as needed
]

# Insert test data into MongoDB collection
devices_collection.insert_many(test_data)

print("Test data populated successfully.")
