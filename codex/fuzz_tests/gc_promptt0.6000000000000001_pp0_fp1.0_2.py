import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
#
# The code in this file is derived from various places:
#    Lib/test/test_gc.py
#    Lib/test/test_weakref.py
#    Lib/test/test_descr.py
#    Lib/test/test_support.py
#
# It has been tweaked to run standalone, outside the regrtest framework.
#

import gc
import unittest
import weakref
from test import test_support

#=======================================================================
# Decorator for skipping tests on non-CPython implementations.

def cpython_only(test):
    """Decorator for skipping tests on non-CPython implementations."""
    import sys
    return test if sys.platform == 'cli' or sys.implementation.name == 'cpython' else None

#=======================================================================
# Uncomment to run tests in verbose mode.
#
#VERBOSE = 1

#=======================================================================
# Utilities

class GCTestBase(unittest.TestCase):
    # Some tests here use gc.garbage
