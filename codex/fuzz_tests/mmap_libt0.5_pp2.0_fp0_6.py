import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import xml.etree.ElementTree as ET

import pycurl

try:
    import simplejson as json
except ImportError:
    import json

try:
    import requests
except ImportError:
    print "Please install requests module: pip install requests"
    sys.exit(1)

try:
    import pycurl
except ImportError:
    print "Please install pycurl module: pip install pycurl"
    sys.exit(1)

try:
    import pytz
except ImportError:
    print "Please install pytz module: pip install pytz"
    sys.exit(1)

try:
    import dateutil.parser
except ImportError:
    print "Please install dateutil module: pip install python-dateutil"
    sys.exit(1)

try:
    import pyasn
except ImportError:
    print "Please install pyasn module: pip install pyasn"
    sys.exit(1
