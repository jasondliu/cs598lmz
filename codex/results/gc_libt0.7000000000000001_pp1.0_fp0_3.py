import gc, weakref
import sys
import unittest
from test import support

class X(object):
    def __del__(self):
        print("deleting X")

class Y(object):
    def __del__(self):
        print("deleting Y")

class Z(X, Y):
    pass

# testing gc.callbacks

class GCTests(unittest.TestCase):

    def setUp(self):
        self.callbacks = gc.callbacks[:]
        gc.callbacks[:] = []

    def tearDown(self):
        gc.callbacks[:] = self.callbacks

    def callback(*args):
        self = args[-1]
        self.callback_args = args[:-1]

    def test_gc_callbacks(self):
        # Check simple callbacks
        self.callback_args = None
        gc.callbacks.append(self.callback)
        gc.collect()
        self.assertNotEqual(self.callback_args, None)

        # Check that the callback
