import mmap
# Test mmap.mmap(0,1,prot=mmap.PROT_READ).find('\0')
import sys
import os
import time
import gc

import unittest
import urllib
import urlparse
import StringIO

try:
  import threading as _threading
except ImportError:
  import dummy_threading as _threading

class devnull(object):
    "Like /dev/null but writable"
    def write(self, s):
        pass

class ValidationError(ValueError):
    pass

class FormParser(object):
    """See `ctypes.test.test_formparser.FormParserTestCase` for documentation.
    """
    _testcase = {} # set by testcase
    FIELD_NAME = 0
    FIELD_VALUE = 1

    class MiniFieldStorage(object):
        # A class which looks a bit like FieldStorage, but is
        # more dict-like, and represents one form field.
        #
        # FieldStorage.read_urlencoded() stores MiniFieldStorage
        # objects, not values, in its
