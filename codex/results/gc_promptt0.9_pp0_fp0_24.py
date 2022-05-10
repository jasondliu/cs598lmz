import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, gc.get_threshold, gc.set_threshold,
# gc.get_count, and gc.garbage.
#
# This test is intended to run under the test_support 'bigmem'
# resource, so it doesn't bother to check for small-memory systems.
#
# We test set_threshold by setting it to thresholds where we expect
# the next collection to collect only a certain kind of object.
# This also tests gc.get_threshold().
#
# Invoke this with:
#                       regrtest.py -R bigmem gc_tests.py

from test import test_support
from unittest import TestCase
import os
import sys
import time
import gc
import weakref

import test_support

def dict_with_size(size):
    # dicts with more than about 20 values aren't very
    # space-efficient, but that's OK for this test
    d = {}
    for i in xrange(size):
        d[i * 10] = i
    return d

# test callback support

