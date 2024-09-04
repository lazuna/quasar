import requests

# GET request
response = requests.get('https://api.example.com/data')
print(response.json())

# POST request
response = requests.post('https://api.example.com/data', json={'key': 'value'})
print(response.status_code)
