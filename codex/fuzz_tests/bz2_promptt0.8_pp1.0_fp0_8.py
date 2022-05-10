import bz2
# Test BZ2Decompressor
import io
dc=bz2.BZ2Decompressor()
data = dc.decompress(data)
io.StringIO(data)

# Set variable to the data
data = r.text

# Load the data
json_data = json.loads(data)


#

# Load the data
json_data = json.loads(data)

# Process and render the map
print(json_data)
import json
import httplib2
import sys
import codecs
from oauth2client.client import GoogleCredentials

CLIENT_SECRETS_FILE = "client_secret.json"

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the APIs Console
https://console.developers.google.com

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client
