import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 7

import sys, os, time, types

# SOURCE LINE 10

import __builtin__

# SOURCE LINE 12

import threading
threading._shutdown = False

# SOURCE LINE 14

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

# SOURCE LINE 18

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

# SOURCE LINE 22

from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api import mail_stub
from google.appengine.api import user_service_stub
from google.appengine.api.memcache import memcache_stub
from google.appengine.api.taskqueue import taskqueue_stub
from google.appengine.api.urlfetch import urlfetch_stub
from google.appengine.
