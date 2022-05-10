import types
types.ModuleType.__init__ = types.ModuleType.__init__

import sys
import os
import re
import time
import urllib
import urllib2
import cookielib
import threading
import subprocess
import traceback
import pprint
import json
import random
import string
import logging
import logging.handlers
import ConfigParser
import Queue
import hashlib
import base64
import socket
import errno
import ssl
import platform
import datetime
import shutil
import tempfile
import getpass
import glob
import math
import stat

from optparse import OptionParser
from optparse import OptionGroup
from optparse import OptionValueError

# Python 2.6/2.7
try:
    import json
except ImportError:
    import simplejson as json

# Python 2.6/2.7
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

# Python 2.6/2.7
try:
    import httplib
except ImportError:
    import http.client as httpl
