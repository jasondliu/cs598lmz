import codecs
codecs.register_error('strict', codecs.ignore_errors)
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

# Download the JSON data from OpenStreetMap nodes near
# San Francisco, California, USA.

OVERPASS_URL = "http://overpass-api.de/api/interpreter"
OVERPASS_QUERY = """
[out:json];
(
  node["amenity"="restaurant"](37.783419,-122.489401,37.829859,-122.366965);
  node["shop"="convenience"](37.783419,-122.489401,37.829859,-122.366965);
  node["cuisine"](37.783419,-122.489401,37.829859,-122.366965);
);
out body;
"""


def get_json(url):
    response = urllib.urlopen(url)
    return json.loads(response.read())


def get_restaurants(filename):
    data = get_
