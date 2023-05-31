import random
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['networksdb']
devices_collection = db['devices']

# Device types and product IDs
device_types = ['Router', 'Switch', 'Firewall']
product_ids = ['CISCO1234', 'CISCO5678', 'CISCO9012']

# Generate test data
test_data = []
for device_type in device_types:
    for _ in range(500):
        device = {
            'hostname': f'{device_type.lower()}{random.randint(1, 999)}',
            'device_type': device_type,
            'serial': f'{random.randint(1000000000, 9999999999):010}',
            'product_id': random.choice(product_ids)
        }
        test_data.append(device)

# Insert test data into MongoDB collection
devices_collection.insert_many(test_data)

print("Test data populated successfully.")
