import io
# Test io.RawIOBase

import _io
import unittest
from test import support

if not hasattr(io, 'RawIOBase'):
    raise unittest.SkipTest('test needs io.RawIOBase')

class RawIOTest(unittest.TestCase):

    def test_abc_override(self):
        # Issue #11649: RawIOBase is an ABC, but its methods do nothing.
        # This test checks that the ABC checkers are not triggered.
        class RawIOSubclass(io.RawIOBase):
            pass
        with RawIOSubclass():
            pass
        with RawIOSubclass():
            pass
        with RawIOSubclass() as rf:
            rf.fileno()
            rf.isatty()
            rf.tell()
            rf.seek()
            rf.readline()
            rf.readlines()
            rf.read()
            rf.readinto1()
            rf.readinto()
            rf.readall()
            rf.write()
            r
