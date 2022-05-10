import weakref
# Test weakref.ref
import unittest
import sys
from test import support, mapping_tests

class TestWeakref(unittest.TestCase):
    def setUp(self):
        self.list = range(10)
        self.double = lambda x: x * 2

    # Create a bunch of instances to use for various tests.
    # Note that these are not garbage collected during the test run.
    # There's not much we can do about it.
    def createInstances(self):
        self.obj = C()
        self.obj.x = 'x'
        self.A = A()
        self.B = B(self.obj)
        self.C = C()
        self.D = D(self.obj)
        self.L = Empty() # Empty class
        self.E = Empty() # Empty subclass
        self.F = Empty() # Empty subclass
        class G:
            def __init__(self, arg):
                self.arg = arg
            def method(self, arg1):
                self.arg1 = arg1
