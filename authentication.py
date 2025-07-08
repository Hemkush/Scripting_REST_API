import requests
import json

url = "https://api.github.com/user"
def get_request(url, headers=None, params=None):
    """
    Perform a GET request to the specified URL with optional headers and parameters.
    
    :param url: The URL to send the GET request to.
    :param headers: Optional dictionary of headers to include in the request.
    :param params: Optional dictionary of query parameters to include in the request.
    :return: The response object from the GET request.
    """
    try:
        response = requests.get(url, headers=headers, params=params)  # You can also pass headers and params if needed
        print("Status Code:", response.status_code)  # Print the status code of the response
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
if __name__ == "__main__":
    # Example: Call the get_request function
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Accept": "application/vnd.github.v3+json"
    }

    get_request(url, headers=headers)


