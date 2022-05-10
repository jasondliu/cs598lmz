import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

# A base class for defining the tests.

class BaseTestRawIO(object):

    # Subclass must define the following attributes:
    #   - self.filename
    #   - self.modes
    #   - self.bprefix

    def setUp(self):
        self.f = io.open(self.filename, 'w+b')
        self.f._checkClosed = lambda: None

    def tearDown(self):
        self.f.close()
        try:
            os.unlink(self.filename)
        except OSError:
            pass

    def test_attributes(self):
        self.assertEqual(self.f.mode, 'w+b')
        self.assertEqual(self.f.name, self.filename)
        self.assertEqual(self.f.closed, False)

    def test_weakref(self):
        p = weakref.proxy(self.f)
