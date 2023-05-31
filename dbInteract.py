from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['networksdb']
devices_collection = db['devices']

def get_device_counts():
    pipeline = [
        {"$group": {"_id": "$device_type", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    device_counts = devices_collection.aggregate(pipeline)
    return device_counts

def list_devices_by_category(category):
    devices = devices_collection.find({"device_type": category})
    return devices

def print_device_counts(device_counts):
    print("Device Counts:")
    for device_count in device_counts:
        category = device_count['_id']
        count = device_count['count']
        print(f"{category}: {count}")
    print()

def print_devices(devices):
    print("Devices:")
    for device in devices:
        print(device)
    print()

def main():
    device_counts = get_device_counts()
    print_device_counts(device_counts)

    category_input = input("Enter a category to list devices (or leave blank to exit): ")
    while category_input:
        devices = list_devices_by_category(category_input)
        print_devices(devices)
        category_input = input("Enter a category to list devices (or leave blank to exit): ")

    # Close the MongoDB connection
    client.close()

if __name__ == '__main__':
    main()
