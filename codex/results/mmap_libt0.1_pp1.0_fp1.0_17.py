import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup

from . import config
from . import utils

class Scraper(object):
    def __init__(self, url, output_dir, verbose=False):
        self.url = url
        self.output_dir = output_dir
        self.verbose = verbose

        self.soup = None
        self.title = None
        self.chapter_urls = []
        self.chapter_titles = []

    def scrape_url(self, url):
        try:
            response = urllib2.urlopen(url)
            return response.read()
        except:
            print 'Error occured: %s' % (traceback.format_exc())
            return ''

    def save_image(self, image_url):
        image_data = self.scrape_url(image_url)
        image_file_name = os.path.join(self.output_
