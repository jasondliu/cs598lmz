import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This test tests the gc module.  It is separate so that tests can
# use gc without causing untimely collections.

import sys
import gc
import weakref
import unittest
import operator
import copy
import gc
import os
import pickle
import time
import threading
import weakref

from test.support import run_unittest, gc_collect, check_impl_detail
from test import support

class GCTests(unittest.TestCase):
    def test_gc_disabled(self):
        # Issue #5095: if gc is disabled, collecting still occurs
        # at exit.
        rc = gc.get_threshold()
        gc.disable()
        try:
            gc.collect()
        finally:
            gc.set_threshold(*rc)

    def test_count(self):
        # Test GC debug option
        gc.set_debug(gc.DEBUG_STATS)
        old_stats = gc.get_stats()
        gc.collect()
        new_
