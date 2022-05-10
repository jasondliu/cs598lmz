import codecs
codecs.register_error("strict", codecs.ignore_errors)
import re
import os
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

"""
This script was written to extract the names and addresses of the restaurants from the Just Eat API.
You will have to provide your own API key. 
The API documentation can be found at: https://github.com/justeat/apistylebook/wiki/API-Reference
"""

"""
Script that extracts restaurant information from the API of Just Eat. 
It will extract a list of restaurant names and their associated addresses,
which are located in the York area. 

All information will be saved as a tab-separated table. 
"""

# Credentials
# Use your own credentials
username = 'USERNAME'
password = 'PASSWORD'
key = 'API-KEY'

# Open output file
output = codecs.open('restaurants.tsv', 'wb', 'utf-8')

# Write the header to the output file
output.write('Restaurant\tAddress\n')


