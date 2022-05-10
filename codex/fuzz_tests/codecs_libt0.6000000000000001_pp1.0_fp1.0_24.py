import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Define the parameters
params = {
    'api_key': 'd240c03e7a2a37b8d8f01f4a6adf1e0b',
    'primary_release_year': '2018',
    'language': 'en-US'
}

# Get the data from the API
response = requests.get('https://api.themoviedb.org/3/discover/movie', params=params)

# Print the status code of the response.
print(response.status_code)

# Save the data to a file
f = open('data.txt', 'w')
f.write(json.dumps(response.json(), indent=4))
f.close()
