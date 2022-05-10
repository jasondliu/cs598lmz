import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import os
import sys
import logging
import time
import traceback
import subprocess
import tempfile
import shutil
import signal
import errno
import random
import socket
import urlparse
import datetime
import re
import json
import hashlib
import functools
import collections
import tempfile
import base64
import cgi
import urllib
import urllib2
import httplib
import ssl
import ConfigParser
import StringIO
import zipfile
import contextlib
import argparse
import getpass
import platform
import locale
import locale
import stat
import tempfile
import fnmatch
import pwd
import grp
import hashlib
import copy
import math
import json

# python 2.5 compat
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

try:
    import argparse
except ImportError:
    print "Please install python-argparse package"
    sys.exit(1)
