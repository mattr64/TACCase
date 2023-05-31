import json
import requests

def convert_to_serializable(data):
    if isinstance(data, dict):
        return {str(key): convert_to_serializable(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, (int, float, str, bool)):
        return data
    else:
        return str(data)

def get_device_details(hostname):
    url = f'http://localhost:5001/api/devices/{hostname}'
    response = requests.get(url)
    if response.status_code == 200:
        device_details = response.json(object_hook=convert_to_serializable)
        return device_details
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None