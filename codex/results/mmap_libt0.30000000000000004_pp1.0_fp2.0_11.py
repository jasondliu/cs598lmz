import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urlparse
import xml.dom.minidom

from xml.sax.saxutils import escape

from util import *

def get_url_data(url):
    """
    Get the data from a URL.
    """
    try:
        return urllib.urlopen(url).read()
    except IOError, e:
        print >> sys.stderr, "Error opening URL: %s" % url
        raise e

def get_url_data_cached(url, cache_dir):
    """
    Get the data from a URL, caching it in the given directory.
    """
    url_hash = hashlib.md5(url).hexdigest()
    cache_file = os.path.join(cache_dir, url_hash)
    if os.path.exists(cache_file):
        try:
            return open(cache_file).read()
        except IOError, e:
            print >> sys.stderr, "
