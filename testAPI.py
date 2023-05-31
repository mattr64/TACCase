from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/api/open-case', methods=['POST'])
def open_case():
    # Get the request data
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    hostname = data.get('hostname')
    contact_name = data.get('contactName')
    contact_email = data.get('contactEmail')
    contact_phone = data.get('contactPhone')

    # Query NetworksDB API to get device type, serial, and product ID
    networks_db_api = 'http://10.64.1.2'
    networks_db_endpoint = f'{networks_db_api}/devices/{hostname}'
    response = requests.get(networks_db_endpoint)
    
    if response.status_code == 200:
        device_data = response.json()
        device_type = device_data.get('device_type')
        serial = device_data.get('serial')
        product_id = device_data.get('product_id')
        
        # Open case with Cisco TAC using retrieved information
        cisco_tac_api = 'https://tac-api.cisco.com'
        cisco_tac_endpoint = f'{cisco_tac_api}/cases'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_TAC_API_TOKEN'  # Replace with your actual TAC API token
        }
        case_data = {
            'title': title,
            'description': description,
            'deviceType': device_type,
            'productID': product_id,
            'serialNumber': serial,
            'caseType': 'Technical',
            'priority': 'P3',
            'engineerType': 'NONE',
            'contactInfo': {
                'contactName': contact_name,
                'contactEmail': contact_email,
                'contactPhone': contact_phone
            }
        }
        response = requests.post(cisco_tac_endpoint, json=case_data, headers=headers)
        
        if response.status_code == 201:
            return f"Case opened successfully for device {hostname} with type {device_type}, serial {serial}, and product ID {product_id}."
        else:
            error_message = response.json().get('message', 'Failed to open case with Cisco TAC.')
            return f"Error opening case with Cisco TAC: {error_message}"
    else:
        return "Failed to retrieve device information from NetworksDB."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
