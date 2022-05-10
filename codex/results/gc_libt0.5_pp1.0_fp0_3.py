import gc, weakref
import operator
import sys
import time
import unittest

class TestCase(unittest.TestCase):

    def test_weakref_callbacks(self):
        # Issue #16602: weakref callbacks on objects with a __del__ method
        # are not called if the object has a __weakref__ slot.
        #
        # We test this by creating a cycle involving an object with a
        # __del__ method and a weak reference to it.
        #
        # The callback should be called when the weak reference is
        # cleared, and the object should be collected.
        #
        # We also check that the callback is called with the weak reference
        # as its first argument.
        #
        # We check that the __del__ method is called after the callback.
        #
        # We check that the callback is called before the object is
        # finalized.
        #
        # We check that the callback is called even if the __del__ method
        # raises an exception.
        #
        # We check that the callback is not called if the weak reference
        # is not
