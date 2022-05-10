import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys
import os
import re
import time
import threading
import traceback
import logging
import logging.handlers
import cStringIO
import warnings
import weakref
import functools
import itertools
import collections

# SOURCE LINE 18

import pkg_resources

# SOURCE LINE 20

from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api import mail_stub
from google.appengine.api import urlfetch_stub
from google.appengine.api import user_service_stub
from google.appengine.api import images_stub
from google.appengine.api import logservice_stub
from google.appengine.api import memcache_stub
from google.appengine.api import taskqueue_stub
from google.appengine.api import xmpp_service_stub
from google.appengine.api import apiproxy_
