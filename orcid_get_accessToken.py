import requests

# Set the API endpoint and your client ID and client secret
api_endpoint = "https://orcid.org/oauth/token"
client_id = "Your Client id" # You can learn it via your orcid account.
client_secret = "Your secret id" # You can learn it via your orcid account too.

# Set the authorization header and payload
headers = {
    "Accept": "application/json",
}
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials",
    "scope": "/read-public",
}

# Send the request to the API endpoint
response = requests.post(api_endpoint, headers=headers, data=data)

# Check the status code of the response
if response.status_code == 200:
    # If the request is successful, the access token will be in the response
    access_token = response.json()["access_token"]
    print("Access token:", access_token)
else:
    # If the request is not successful, print the error message
    # print("Error:", response.json()["error"]) # This is problem for now.
    print('Error Message !!!')
