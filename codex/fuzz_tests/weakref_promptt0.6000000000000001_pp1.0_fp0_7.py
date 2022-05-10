import weakref
# Test weakref.ref.__repr__
import operator
import unittest
from test import support

class ReprTest(unittest.TestCase):

    def test(self):
        # See issue #4434: weakref.ref.__repr__ should not fail if the
        # referent is not available anymore.

        class Foo(object):
            def __init__(self, name):
                self.name = name
            def __del__(self):
                print("Deleting {}".format(self.name))

        foo = Foo("foo")

        # Create a weak reference to foo
        ref = weakref.ref(foo)

        # Delete foo
        del foo

        # Get the repr of the weak reference
        repr(ref)

        # Get the repr of the weak reference again
        repr(ref)


class Base(object):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C, D):
    pass


