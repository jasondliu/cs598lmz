import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import json
import logging
import multiprocessing
import os
import re
import shutil
import urllib
import urllib2

from bs4 import BeautifulSoup
from PIL import Image

import config
import db
import download
import util

logging.basicConfig(level=logging.DEBUG)

def get_page(url):
    """
    Retrieve the content of the given URL.
    """
    try:
        logging.debug('Retrieving %s' % url)
        response = urllib2.urlopen(url)
        return response.read()
    except urllib2.HTTPError as e:
        logging.error('HTTP error %s' % e.code)
        raise e
    except urllib2.URLError as e:
        logging.error('URL error %s' % e.reason)
        raise e

def get_images(url):
    """
    Retrieve all the
