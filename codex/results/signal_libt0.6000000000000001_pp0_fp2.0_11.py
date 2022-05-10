import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import re
import sys
import time
import math
import codecs
import re
import urllib
import urllib2
import urlparse
import socket
import datetime
import StringIO
import logging
import logging.config
import traceback
import base64
import json
import uuid
import hashlib
import zlib

from urllib import urlencode
from urlparse import parse_qs, urlparse

try:
    import xml.etree.ElementTree as ET
except ImportError:
    import elementtree.ElementTree as ET

try:
    import xbmc
except Exception, e:
    pass # for PC debugging

try:
    import xbmcaddon
except Exception, e:
    pass # for PC debugging

try:
    import xbmcgui
except Exception, e:
    pass # for PC debugging

try:
    import xbmcplugin
except Exception, e:
    pass # for PC debugging

try:
    import xbm
