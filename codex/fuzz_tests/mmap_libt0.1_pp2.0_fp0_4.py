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
from bs4 import SoupStrainer
from bs4 import UnicodeDammit

from lib import config
from lib import db
from lib import log
from lib import util

#------------------------------------------------------------------------------
# Globals
#------------------------------------------------------------------------------

# The user agent to use when making HTTP requests.
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'

# The maximum number of times to retry a request.
MAX_RETRIES = 5

# The maximum number of times to retry a request that failed with a server
# error.
MAX_SERVER_ERROR_RETRIES = 10

# The maximum number of times to retry a request that failed with a network
# error.
MAX_NETWORK_ERROR_RETRIES = 10
