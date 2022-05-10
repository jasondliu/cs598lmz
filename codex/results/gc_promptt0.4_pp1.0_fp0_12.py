import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This is a test for the gc module.  It tests the gc.collect() function.
#
# This test is derived from the test for the same function in Python 2.2.
#

import sys
import gc
import unittest
from test import test_support

class GcCollectTestCase(unittest.TestCase):
    # This test is a bit tricky:  it tests gc.collect() indirectly by
    # checking that certain invariants are true before and after calling
    # gc.collect().  The invariants in question are that certain objects
    # are always found (or never found) by gc.collect().
    #
    # The objects we use for the test are tuples t1 and t2, and object x.
    # t1 is a tuple without any references to it.  t2 is a tuple with a
    # reference to it from t1.  x is a mutable object with a reference to
    # it from t2.
    #
    # We arrange things so that t1 is found by gc.collect() and t2
