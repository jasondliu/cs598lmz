import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import time
import urllib

from modules.utils import *
import modules.config as config

class Google:
    def __init__(self, query):
        self.query = query
        self.results = []
        self.totalresults = ""
        self.server = 'www.google.com'
        self.hostname = 'www.google.com'
        self.userAgent = '(Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1)'
        self.quantity = '100'
        self.limit = 100
        self.counter = 0

    def do_search(self):
        h = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1'
        headers = {
