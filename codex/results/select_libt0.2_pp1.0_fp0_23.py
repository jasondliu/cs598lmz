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
# - Max number of cookies is 50.
# - Max cookie size is 4KB.
# - Max number of URL redirects is 10.
# - Max URL length is 2KB.
# - Max URL path component length is 500 bytes.
# - Max URL path depth is 8.
# - Max URL query component length is 500 bytes.
# - Max URL query depth is 8.
# - Max URL fragment length is 500 bytes.
