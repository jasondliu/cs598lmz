import codecs
codecs.register_error('strict', codecs.ignore_errors)

import requests
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
import os
import re
import string
import time
import sys

#from __future__ import print_function

reload(sys)
sys.setdefaultencoding('utf-8')

def get_json(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception, e:
        print e
        return None

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception, e:
        print e
        return None

def get_soup(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'lxml')
    except Exception, e:
        print e

