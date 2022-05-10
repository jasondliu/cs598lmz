import weakref
# Test weakref.ref
import gc

import sys
if sys.version_info < (2, 6):
    import unittest2 as unittest
else:
    import unittest

from threading import Timer

class Callable(object):
    def __call__(self):
        self.called = True

def check_alive(ref, expected_alive):
    if expected_alive == (ref() is not None):
        return True
    print(("The object is %salive but should be %s" %
           ('alive' if expected_alive else 'dead',
            'alive' if not expected_alive else 'dead')))
    return False

class WeakrefTest(unittest.TestCase):

    def test_basic(self):
        callable = Callable()
        ref = weakref.ref(callable)
        self.assertTrue(ref() is callable)
        self.assertTrue(ref() is not None)
        self.assertTrue(callable.called is None)
        del callable
        self.assertTrue
