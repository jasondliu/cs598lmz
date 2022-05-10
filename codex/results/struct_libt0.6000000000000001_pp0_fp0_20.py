import _struct
import _thread
import _threading_local
import _warnings
import _weakref
import array
import atexit
import builtins
import faulthandler
import gc
import itertools
import marshal
import math
import operator
import posix
import pwd
import reprlib
import select
import sys
import sysconfig
import threading
import time
import unicodedata
import zipimport

# Disable the garbage collector when running the tests.
gc.disable()

# Ensure we have an up-to-date copy of the zipimport module.
reload(zipimport)

# Ensure we have an up-to-date copy of the _testcapi module.
reload(_testcapi)

# Import _testcapi again, so that it gets stored in sys.modules.
import _testcapi

# Create a reference to the original _testcapi module to restore it later.
_testcapi_orig = sys.modules['_testcapi']

# Create a copy of the original _testcapi module so that we can restore it
# later, even
