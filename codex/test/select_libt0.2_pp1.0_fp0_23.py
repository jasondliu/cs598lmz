import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2
import urlparse

from lib import config
from lib import control
from lib import helpers
from lib import proxy
from lib import version

# GAE supports http/1.1, but some http/1.1 features are restricted.
# - Max header name or value size is 100 bytes.
# - Max request-line size is 500 bytes.
# - Max number of headers is 50.
# - Max number of parameters is 100.
# - Max parameter size is 100 bytes.
# - Max request body size is 1MB.
# - Max response body size is 32MB.
