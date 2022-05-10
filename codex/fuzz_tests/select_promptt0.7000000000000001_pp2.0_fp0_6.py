import select
# Test select.select
import subprocess
# Test subprocess.Popen
import sys
# Test sys.platform
import time
# Test time.time
import traceback
# Test traceback.format_exc
import unittest
# Test unittest
import urllib
# Test urllib.urlopen
import uuid
# Test uuid.uuid4

# Try these modules (they may not be available on all platforms)
try:
    import bz2
    # Test bz2.BZ2File
    import ctypes
    # Test ctypes.CDLL
    import distutils.dir_util
    # Test distutils.dir_util.mkpath
    import email
    # Test email.message_from_string
    import gdbm
    # Test gdbm.open
    import gzip
    # Test gzip.GzipFile
    import multiprocessing
    # Test multiprocessing.Pool
    import sqlite3
    # Test sqlite3.connect
    import zlib
    # Test zlib.decompress
except ImportError:
    pass

