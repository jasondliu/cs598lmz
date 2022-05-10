from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: self.decompress('0')

import sys
import time
import urllib2
import xml.etree.ElementTree as ET

import requests
import simplejson as json
from requests.exceptions import ConnectionError, Timeout

import util

def get_revisions_for_article(title):
    """
    Get list of revisions for a given article title.

    Revisions are returned as a list in reverse chronological order.
    """
    url = 'http://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvprop=timestamp|user|ids&rvlimit=500&titles=' + urllib.quote(title)
    r = requests.get(url)

    if r.status_code == 200:
        data = json.loads(r.text)
        revisions = [x['revid'] for x in data['query']['pages'].values()[0]['revisions']]
        return revisions
    else:
        return []


def get_revisions(
