import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

# Global variables
version = "0.1"

# Global constants
DEBUG = False

#
# Helper functions
#

def debug(message):
    if DEBUG:
        print >> sys.stderr, "DEBUG:", message

def error(message):
    print >> sys.stderr, "ERROR:", message

def info(message):
    print >> sys.stderr, "INFO:", message

def warning(message):
    print >> sys.stderr, "WARNING:", message

#
# Classes
#

class WebPage(object):
    def __init__(self, url):
        self.url = url
        self.html = ""
        self.links = []

    def fetch(self):
        try:
            # Open the web page
            debug("Opening %s" % self.url)
            request = urllib2.Request(self.url)
            request.add
