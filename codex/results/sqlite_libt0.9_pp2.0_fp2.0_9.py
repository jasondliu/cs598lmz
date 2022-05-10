import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import traceback
import murmur

from lib.config import PYTS3_PATH

# murmur.lib is not found sometimes using ctypes.util.find_library()
# get correctly versioned library name from murmur.i

arch = "64" if sys.maxsize > 2**32 else "32"
includefile = "%s/murmur/src/murmur.i" % PYTS3_PATH
includefile = os.path.normpath(includefile)
with open(includefile, 'r') as f:
    preamble_data = f.read()
preamble_data = preamble_data.split('%include')
preamble_data = preamble_data[1].split('\n')

lib_data = preamble_data[1].strip().replace('"', '')
lib_data = lib_data.replace('lib', '')
lib_data = lib_data.replace('.so', '')
lib_data = lib_data.replace('-
