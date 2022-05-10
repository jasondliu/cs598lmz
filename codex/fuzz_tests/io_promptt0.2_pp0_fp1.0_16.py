import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support
from test.support import import_helper

# Base for testing the IOBase ABC.
class BaseTestIO(object):

    def test_abc(self):
        self.assertTrue(issubclass(self.thetype, _io.IOBase))

    def test_attributes(self):
        f = self.thetype()
        self.assertEqual(f.mode, None)
        self.assertEqual(f.name, None)
        f.close()

    def test_weakref(self):
        f = self.thetype()
        p = weakref.proxy(f)
        self.assertEqual(p.mode, None)
        self.assertEqual(p.name, None)
        f.close()

    def test_close(self):
        f = self.thetype()
        f.close()
        self.assertEqual(f.closed, True)
        f.close()
        self.assertEqual(f.closed, True
