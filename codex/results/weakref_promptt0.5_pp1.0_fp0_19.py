import weakref
# Test weakref.ref()
import pickle
import copy
import sys
import unittest

class C:
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return 'C(%r)' % self.arg

class D:
    pass

class E(D):
    pass

class F(D):
    pass

class G(D):
    pass

class H(D):
    def __init__(self, arg):
        self.arg = arg

class I(D):
    def __init__(self, arg):
        self.arg = arg

class J(D):
    def __init__(self, arg):
        self.arg = arg

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        # Test basic weakref operations
        o = C(1)
        p = C(2)
        q = C(3)
        r = C(4)
        s = C(5)
        w = weakref.ref(
