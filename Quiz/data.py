import requests

parameters = {
    'amount' : 10,
    'type' : 'boolean'
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()

# Create a list of Question objects using data from the API response
question_data = data['results']



