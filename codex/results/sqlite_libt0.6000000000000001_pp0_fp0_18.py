import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import sys
import os.path
import re
import json
import traceback
import subprocess
import Queue
import struct
import glob
import getpass
import platform
import shutil
import base64

from collections import defaultdict, namedtuple

try:
    import argparse
except ImportError:
    argparse = None

try:
    import readline
except ImportError:
    readline = None

#
# Python 2.7 compatability:
#

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

try:
    from urllib.parse import quote_plus, unquote_plus
except ImportError:
    from urllib import quote_plus, unquote_plus

try:
    unicode
except NameError:
    unicode = str

try:
    xrange
except NameError:
    xrange = range

try:
    import urllib2
    HTTPError = urllib2.HTTPError
except ImportError:

