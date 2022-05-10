import codecs
# Test codecs.register_error

import sys
import string
from test_support import TestFailed, run_unittest
# Test asynchronous generator functions.
import asyncio

# Make sure sys.exc_info() works

# Test sys.exc_clear()

class _C:
    def __getattr__(self, name):
        raise AttributeError(name)

    def __repr__(self):
        return '_C'

_x = _C()

class TestException(unittest.TestCase):

    def test_sysexc_info(self):
        try:
            raise _x
        except AttributeError:
            try:
                raise
            except:
                t, v, tb = sys.exc_info()

        self.assertEqual(t, AttributeError)
        self.assertEqual(v, _x)

    def test_sysexc_clear(self):
        try:
            raise _x
        except AttributeError:
            t, v, tb = sys.exc_info()

        self.assertEqual(t
