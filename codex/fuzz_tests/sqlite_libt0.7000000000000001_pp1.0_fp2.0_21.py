import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import re
import math
import getpass
import struct
import select
import socket

PY3 = sys.version_info[0] == 3

if PY3:
    import urllib.parse
    import urllib.request
else:
    import urllib2
    import urllib

try:
    import crcmod
    crcfunc = crcmod.mkCrcFun(0x11021, initCrc=0, rev=False)
except Exception:
    crcfunc = None

try:
    import queue
except ImportError:
    import Queue as queue

# this is a list of all the devices we know about
# and their names and locations
# note that we are also using the device name in the
# key so that we can have more than one of the same
# device and it will know which one is which
# we might need to change this later so that we can
# have multiple of the same device but for now
# let's just use the device name

# devices from /dev/

