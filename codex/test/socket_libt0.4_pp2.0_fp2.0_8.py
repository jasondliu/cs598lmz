import socket
import sys
import time
import urllib
import urllib2
import urlparse

import requests

from . import exceptions
from . import utils

# Python 2.6 compat
try:
    import json
except ImportError:
    import simplejson as json


