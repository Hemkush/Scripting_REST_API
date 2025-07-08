import requests
import json

url = "https://jsonplaceholder.typicode.com"
response = requests.get(f"{url}/todos/1")
if response.status_code == 200:
    data = response.json()
    print("Response JSON:", data)
    print("Response ID:", json.dumps(data, indent=4))

response = requests.get(f"{url}/users")

try:
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    users = response.json()
    print("Users:", json.dumps(users, indent=4))
except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)

# Example of a POST request

jsonPayload = {
    "userId": 11,
    "id": 201,
    "title": "New title",   
    "completed": False
}

responsePost = requests.post(f"{url}/todos", json=jsonPayload)
print("Response JSON:", responsePost.json())

# Example of a PUT request
responsePut = requests.put(f"{url}/todos/1", json=jsonPayload)
print("Response JSON for PUT:", responsePut.json())
# Example of a DELETE request
responseDelete = requests.delete(f"{url}/todos/1")
print("Response JSON for DELETE:", responseDelete.json())

