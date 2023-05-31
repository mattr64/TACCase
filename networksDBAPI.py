from flask import Flask, jsonify
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['networksdb']
devices_collection = db['devices']

@app.route('/api/devices/<hostname>', methods=['GET'])
def get_device_info(hostname):
    device = devices_collection.find_one({'hostname': hostname})
    if device:
        try:
            device['_id'] = str(device['_id'])  # Convert ObjectId to string
            return jsonify(device)
        except TypeError as e:
            print(f"Serialization error: {e}")
            return jsonify({'error': 'Unable to serialize device data.'}), 500
    else:
        return jsonify({'error': 'Device not found.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
