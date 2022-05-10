import codecs
# Test codecs.register_error('ignore')
import glob
import os
import sys

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse

# Import BeautifulSoup -- try 4 first, fall back to older
try:
    from bs4 import BeautifulSoup
except ImportError:
    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        print('We need BeautifulSoup, sorry...')
        sys.exit(1)


class Scraper(object):
    def __init__(self, url):
        """
        Initialize a generic scraper object.
        """
        self.url = url
        self.soup = None

    def load_page(self):
        """
        Load the page and create the BeautifulSoup instance.
        """
        request = urllib2.urlopen(self.url)
        soup = BeautifulSoup(request)
        self.soup = soup

    def write
