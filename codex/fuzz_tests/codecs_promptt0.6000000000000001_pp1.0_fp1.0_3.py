import codecs
# Test codecs.register_error('htmlreplace', codecs.replace_errors)
import csv
import json
import os
import re
import sys
import time

# ################
# ### Settings ###
# ################

# For more information about how to use this script, please visit:
# http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

# The API key to use. 
# To get your API key, sign up at http://www.mashape.com
mashape_key = "YOUR_API_KEY_HERE"

# The API endpoint to use. Currently supported values are "sandbox" and "production"
# To move to production, sign up at http://labs.mashape.com/docs/services/5a3a9b0e76e7d7292a5a5b8d
mashape_endpoint = "sandbox"

# The filename to process
filename = "example.pdf"

# The language of the input document, as an ISO 639
