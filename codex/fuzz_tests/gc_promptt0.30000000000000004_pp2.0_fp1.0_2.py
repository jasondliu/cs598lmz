import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is designed to ensure that gc.collect() is working correctly.
#
# The test does not attempt to test the correctness of the garbage collector
# itself.  It merely tests that gc.collect() does the right thing in various
# situations.

import gc
import weakref
import unittest
import sys
import os
import warnings
import contextlib

from test import support

# Test gc.collect()

class GCTests(unittest.TestCase):
    # In addition to calling gc.collect(), this function also calls
    # gc.set_debug() to enable generation collection.  This is necessary
    # to ensure that all objects are deallocated.
    def collect(self):
        gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
        gc.collect()
        gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

    def test_simple_objects(self):
        # Test gc.collect() on simple objects.
        class A:

