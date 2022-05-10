import weakref
# Test weakref.ref() and weakref.proxy()
#
import weakref
import unittest
import sys

class C(object):
    pass

class D(C):
    pass

class E(C):
    pass

class F(D, E):
    pass

class Base:
    pass

class Derived(Base):
    pass

# Subclass Base and Derived, just to make sure the subclassing
# machinery works with weakrefs.
class Base2(Base):
    pass

class Derived2(Derived):
    pass

class Widget:
    def __del__(self):
        self.deleted = 1

class Widget2:
    pass

class Widget3:
    def __hash__(self):
        return hash(id(self))

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        o = C()
        r = weakref.ref(o)
        self.assertEqual(r(), o)
        self.assertEqual(r.__class__,
