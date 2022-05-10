import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse

from cStringIO import StringIO
from datetime import datetime
from email.utils import parsedate_tz, mktime_tz
from optparse import OptionParser
from subprocess import Popen, PIPE
from threading import Thread

# This is not available in the App Engine SDK.
try:
  import pycurl
except ImportError:
  pycurl = None

# This is not available in the App Engine SDK.
try:
  import ssl
except ImportError:
  ssl = None

# This is not available in the App Engine SDK.
try:
  import win32api
except ImportError:
  win32api = None

# This is not available in the App Engine SDK.
try:
  import win32con
except ImportError:
  win32con = None

# This is not available in the App Engine SDK.
try:
  import win32file

