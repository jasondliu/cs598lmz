import weakref
# Test weakref.ref on callables.

def foo():
    pass

foo_ref = weakref.ref(foo)
del foo
print(foo_ref())
# coverage: ignore
# (we don't care if the test actually runs here)
import weakref
# Shut up pyflakes.
weakref.ref
# Check the repr of a weakref without the referent.

import weakref
# coverage: ignore
# (we don't care if the test actually runs here)
weakref.ref(None).__repr__
# Check the repr of a weakref with the referent.

# coverage: ignore
# (we don't care if the test actually runs here)
import weakref
# Shut up pyflakes.
weakref.ref(7).__repr__
# Check the repr of a ref to None

import weakref

import unittest
from test import support

class Foo(object):
    pass

class TypedWeakrefTest(unittest.TestCase):
    def check_repr(self, r, string):
        rval = r.__repr
