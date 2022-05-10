import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import traceback
import shutil
import time
import datetime
import struct
import netaddr
import uuid
import random
import tempfile
import hashlib
import platform
import stat
import resource
import re
#import subprocess
import statvfs
import unicodedata

# from ctypes import *
from ctypes.util import find_library
from ctypes.wintypes import *

try:
  from cStringIO import StringIO
except:
  from StringIO import StringIO



# FIXME: replace this with using ctypes to dynamically load the libraries and
#        their symbols at runtime.

# NOTE: It's not possible to use a symbolic link in the library path.  Instead
#       make a hard link to the physical library.  See `ln' man page.

# WIN32
try:
  if platform.system() == 'Windows':
    # If python was built with MSVC then the runtime libraries must be
    # redistributed with any program that uses ctypes.  For more information
    # see: http://docs.python.org/2
