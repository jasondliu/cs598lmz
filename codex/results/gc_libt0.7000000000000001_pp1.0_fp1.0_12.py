import gc, weakref
import unittest
import warnings

from weakref import proxy
from test import test_support

################################################################################
# Decorator for skipping tests on non-CPython implementations.

try:
    from _testcapi import getargs_w
except ImportError:
    def CPython(test):
        return lambda x: None
else:
    def CPython(test):
        def decorator(func):
            def wrapper(self):
                if getargs_w() == 'PyPy':
                    raise unittest.SkipTest('test only valid on CPython')
                func(self)
            return wrapper
        return decorator

################################################################################
# Test WeakKeyDictionary

class TestWeakKeyDictionary(unittest.TestCase):

    def test_basic(self):
        class C(object):
            pass
        a = C()
        b = C()
        d = weakref.WeakKeyDictionary(dict.fromkeys([a]))
        self.assertEqual(d[a], None)
        self.assertRaises(KeyError, d.
