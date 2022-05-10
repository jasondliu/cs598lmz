import select
import sys
import urllib2
import re
from optparse import OptionParser
from datetime import datetime
import time

# The size of a chunk of HTML from a urllib2 response
CHUNK_SIZE = 1024

# Time between polling in seconds
SLEEP_TIME = 5

def clean(string):
    """ Removes HTML tags from string """
    return re.sub('<[^<]+?>', '', string)
    
def main():
    usage = "usage: %prog [options] url"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--force", action="store_true", default=False, dest="force", help="force the scraper to run")
    parser.add_option("-p", "--poll", action="store_true", default=False, dest="poll", help="poll the scraper until it is finished")
    
    (options, args) = parser.parse_args()
    
    # Check that the url has been specified
    if len(args) != 1:

