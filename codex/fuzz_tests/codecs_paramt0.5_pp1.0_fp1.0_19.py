import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Python 2.x
try:
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError:
    # Python 3.x
    from urllib.request import urlopen
    from urllib.parse import urlencode

import json
import os

# Set to True to enable debugging output
DEBUG = False

# Set to your API key
API_KEY = os.environ.get('API_KEY')

# API constants, you shouldn't have to change these.
API_HOST = 'https://maps.googleapis.com/maps/api/geocode/json'

# Defaults for our simple example.
DEFAULT_TERM = 'restaurant'
DEFAULT_LOCATION = 'Seattle, WA'

# A request to the Places API.
def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.

    Args:
        host (str): The
