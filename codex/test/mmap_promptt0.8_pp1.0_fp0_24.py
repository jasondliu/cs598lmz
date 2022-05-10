import mmap
# Test mmap.mmap(0) on posix
# Requires Python 2.3
# Ensure large file support is enabled on Windows
from test import test_support
import gc
import sys
from StringIO import StringIO
from time import time as current_time
import os
import unittest
from UserString import UserString
from UserList import UserList
import functools
import random

try:
    from _testcapi import getargs_b
except ImportError:
    getargs_b = None

# Timing tests are not enabled on Jython
IS_TIMING_TEST = test_support.is_resource_enabled('timing')

class BaseTestCase(unittest.TestCase):
    # Base class for testing longs.

    # Sets up the test case by creating a bunch of longs with various
    # values.  self.values is a list of tuples of the form (string
    # value, integer value, long value).
    def setUp(self):
        self.values = []
