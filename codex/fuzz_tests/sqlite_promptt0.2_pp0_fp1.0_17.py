import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import os
import sys
import time
import traceback
import logging
import logging.handlers
import subprocess
import signal
import socket
import select
import struct
import errno
import fcntl
import re
import tempfile
import shutil
import hashlib
import base64
import random
import string
import json
import urllib
import urllib2
import urlparse
import zlib
import gzip
import StringIO
import ConfigParser
import collections
import platform
import struct
import binascii
import math
import ctypes
import ctypes.util
import threading
import sqlite3

from ctypes import *

from xlog import getLogger
xlog = getLogger("gae_proxy")
xlog.set_buffer(500)

current_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(current_path, os.pardir, os.pardir
