import weakref
# Test weakref.ref() and weakref.proxy() for Python objects.
import unittest
from test import test_support
class A:
    pass
class B(A):
    pass
class C(A):
    pass

class D(B, C):
    pass

class E(object):
    pass

class F(object):
    def __init__(self, value=0):
        self.value = value
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return self.value == other.value

class G(F):
    pass

class H(F):
    pass

class I(G, H):
    pass

class J(F):
    def __init__(self, value=1):
        F.__init__(self, value)

class K(F):
    def __init__(self, value=2):
        F.__init__(self, value)

