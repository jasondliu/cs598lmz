import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when an object is both in pending and finalizers lists.
from test.support import run_unittest, TESTFN, gc_collect
from test.support import captured_stderr
from test import test_support

import unittest
import sys
import weakref
import os
from types import FunctionType
import gc

from test.support import gc_collect


class TestExplicitFinalize(unittest.TestCase):

    def setUp(self):
        self.called = []

    def callback(*args):
        self = args[0]
        del args
        self.called.append(None)

    def test_callback_in_del(self):
        # Explicit finalizers run when an object is collected
        # even if __del__ adds a new reference cycle.
        class C(object):
            def __del__(self):
                self.callback = TestExplicitFinalize.callback
                self.callback()

        a = C()
        a.a = a
        wr = weakref.ref(a)
        del a
        gc.collect
