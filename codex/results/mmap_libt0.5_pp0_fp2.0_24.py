import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom

if sys.version_info[0] >= 3:
    import http.client as httplib
    import urllib.parse as urllib
else:
    import httplib
    import urllib

try:
    import json
except ImportError:
    import simplejson as json

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

try:
    import pycurl
except ImportError:
    pycurl = None

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from PIL import Image
except ImportError:
    import Image

try:
    import magic
except ImportError:
    magic = None

try:
    import oauth2 as oauth
except ImportError:
    oauth = None

try:
    import pyex
