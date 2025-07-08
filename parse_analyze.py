import requests
import json

url = "https://jsonplaceholder.typicode.com"
response = requests.get(f"{url}/users")

try:
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    users = response.json()
    print("Users:", json.dumps(users, indent=4))
except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)

for user in users:
    print(f"User ID: {user['id']}, Name: {user['id']}, Username: {user['username']}, Zipcode: {user['address']['zipcode']}")
    
for key, value in user.items():
        print(f"{key}: {value}")