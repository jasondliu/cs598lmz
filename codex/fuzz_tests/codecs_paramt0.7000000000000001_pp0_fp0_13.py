import codecs
codecs.register_error('strict', codecs.ignore_errors)
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
from lxml import html
import os, time
from pyquery import PyQuery as pq

from models import *
from utils import *
from rss_utils import *

import logging

# RSS class
class Rss(webapp2.RequestHandler):
    def get(self):
        logging.info(self.request.path)
        # For logging
        if self.request.path == '/' or self.request.path == '/rss':
            self.redirect('/rss/home')
            return
        logging.info(self.request.path)
        # Get url from url path
        path_parts = self.request.path.split('/')
        if len(path_parts) < 3:
            self.redirect('/rss/home')
            return
        url = '/'.join(path_parts[2:])
        # Get rss
        body = self.get_rss(url)
       
