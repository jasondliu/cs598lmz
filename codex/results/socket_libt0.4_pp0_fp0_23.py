import socket
import urllib.request

# Define the URL to fetch the JSON data from.
url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'

# Open the URL and read the data.
response = urllib.request.urlopen(url, timeout=5)
data = response.read().decode('utf-8')

# Load the JSON data into a Python variable.
data = json.loads(data)

# Print out the current price of Bitcoin in USD.
print(data['bpi']['USD']['rate'])
