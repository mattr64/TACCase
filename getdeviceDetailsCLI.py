import argparse
import json
import requests
from bson import ObjectId

def convert_to_serializable(data):
    if isinstance(data, dict):
        return {str(key): convert_to_serializable(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    elif isinstance(data, (int, float, str, bool)):
        return data
    else:
        return str(data)

def get_device_details(hostname):
    url = f'http://localhost:5001/api/devices/{hostname}'
    response = requests.get(url)
    if response.status_code == 200:
        device_details = json.loads(response.content, object_hook=convert_to_serializable)
        return device_details
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retrieve device details from NetworksDB API.')
    parser.add_argument('hostname', type=str, help='Hostname of the device')
    args = parser.parse_args()

    device_details = get_device_details(args.hostname)
    if device_details:
        print("Device Details:")
        print(json.dumps(device_details, indent=4))
