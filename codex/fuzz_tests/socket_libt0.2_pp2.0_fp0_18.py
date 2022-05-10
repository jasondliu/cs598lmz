import socket
import sys
import time
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup

from . import config
from . import utils
from . import __version__

# TODO:
# - add a timeout to the socket
# - add a timeout to the urllib2
# - add a timeout to the urllib2 opener
# - add a timeout to the urllib2 opener socket
# - add a timeout to the urllib2 opener socket connect
# - add a timeout to the urllib2 opener socket connect timeout
# - add a timeout to the urllib2 opener socket connect timeout socket
# - add a timeout to the urllib2 opener socket connect timeout socket connect
# - add a timeout to the urllib2 opener socket connect timeout socket connect timeout
# - add a timeout to the urllib2 opener socket connect timeout socket connect timeout socket
# - add a timeout to the urllib2 opener socket connect timeout socket connect timeout socket connect
# - add a timeout to the urllib2 opener socket connect timeout socket connect timeout socket connect timeout
# -
