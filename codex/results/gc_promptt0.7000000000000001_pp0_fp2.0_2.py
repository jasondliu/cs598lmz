import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test makes sure that gc.collect() returns the number of objects
# collected, and that unreachable objects with a __del__() method are
# called.

# This test also tries to make sure that no objects are collected or have
# their __del__() method called more than once.  This is a little tricky
# in Python because __del__() methods can resurrect objects.  This test
# doesn't try very hard to detect multiple collections of the same
# object; it just makes sure that each object is collected at most once.
# See the TEST_TARGET_SIZE constant below.  With TEST_TARGET_SIZE=1000,
# the test runs in about 3 seconds on a Sun Ultra 5/270.

import os
import sys
import gc
import unittest
from test import support
from collections import Counter

# Put the Python test objects directory first in sys.path, so this test
# will run the "real" test_gc.py, not the one in the build directory.
test_support = support.import_module('test', deprecated=True)
if __name__ ==
