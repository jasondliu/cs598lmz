import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'))
        self.assertTrue(hasattr(io.RawIOBase, 'name'))

    def test_raw_io_dealloc(self):
        # Issue #11647: the tp_dealloc handler for RawIO instances wasn't
        # properly decref'ing its owned objects.
        rawio = io.RawIOBase()
        r = weakref.ref(rawio)
        del rawio
        self.assertIs(r(), None)

    def test_raw_io_errors(self):
        # Issue #11647: the tp_dealloc handler for RawIO instances wasn't
        # properly setting the exception state when it failed.
        rawio = io.RawIOBase()
        rawio.__class__.close = lambda *args: 1/0
        r = weakref.ref(raw
