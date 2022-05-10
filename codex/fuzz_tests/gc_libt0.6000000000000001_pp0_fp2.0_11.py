import gc, weakref
import os, sys
import time
import types
import weakref
import unittest

from test import test_support

#==============================================================================

# A trivial class to test weak references to objects, and to test the callback
# machinery.
class C:
    pass

class Callback:
    def __init__(self, x):
        self.x = x
    def __call__(self, wr):
        self.x.append(wr)

#==============================================================================

class BasicTestCase(unittest.TestCase):

    def test_basic(self):
        x = C()
        x.a = x
        x.b = C()
        x.b.a = x
        x.b.b = x.b
        wr = weakref.ref(x)
        y = wr()
        self.assertEqual(y, x)
        self.assertEqual(y.a, x)
        self.assertEqual(y.b, x.b)
        self.assertEqual(y.b.a, x)
       
