import mmap
import re
import shutil
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.api import taskqueue
from google.appengine.api import urlfetch
from google.appengine.ext import db
from google.appengine.ext import webapp

from lxml import etree

from markdown import markdown

import site_config

page_template = site_config.page_template
page_header = site_config.page_header

# build an xpath function
xpath_func = etree.XPath("//h5")

def read_dat_file(datname, pagename):
    """
        Read file in the dat directory and return it as a string
    """
    filename = os.path.join(os.path.dirname(__file__), './static/dat/'+datname+'.txt')
    f = open(filename, "r")
    data = f.read()
    f.close()
    #search = re.search(r'\[\[([^
