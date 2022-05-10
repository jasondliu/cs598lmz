import weakref
import sys
import os
import urllib
import urllib2
import json

# get the path to the directory that contains this file
# and add it to the system path
this_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(this_path)

import config

# these are the API endpoints that we will use
# to query YNAB
api_endpoints = {
    "accounts": "accounts",
    "budgets": "budgets",
    "categories": "categories",
    "payees": "payees",
    "transactions": "transactions"
}

class YNAB(object):
    """
    This is the main class that handles all the API calls
    to YNAB.
    """

    def __init__(self):
        """
        Initialize the YNAB class.
        """

        # create a session to store the access token
        self.session = requests.Session()

        # get the access token
        self.get_
