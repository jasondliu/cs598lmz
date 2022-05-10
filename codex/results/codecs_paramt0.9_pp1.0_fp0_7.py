import codecs
codecs.register_error('replace_with_cp500', lambda e: ('', e.start + 1))

def unidecode(x):
	return x.encode('cp500', 'replace_with_cp500').decode('ascii', 'ignore')

import json
import pandas as pd

# import gspread # for Google Spreadsheets

pretty_printer = pprint.PrettyPrinter(indent=4)


# read the Profiles
# get the api key from the environment
key = os.environ['FIAASCO_API_KEY']
# base url for the queries
url_base = 'http://fiascos.qmul.ac.uk/cgi-bin/api.cgi?q='

# make the actual api call based on the persons name (id)
def makecall(person):
	url = url_base + 'profile&profile=' + person + '&key=' + key
	response = urllib.request.urlopen(url)
	data = json.load(response)
	return data

# dump the result of the api call in a json file
