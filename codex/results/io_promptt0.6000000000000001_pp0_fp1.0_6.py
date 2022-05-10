import io
# Test io.RawIOBase
import _io
# Test _io.FileIO
import unittest
import weakref

from test.support import TESTFN, unlink, run_unittest, run_with_locale

# Test the 'io' module

# Test io.FileIO
class TestFileIO(unittest.TestCase):

    def setUp(self):
        self.f = io.FileIO(TESTFN, 'w+')
        self.f.write(bytes(bytearray(range(256))))
        self.f.close()
        self.f = io.FileIO(TESTFN, 'r+')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_invalid_mode(self):
        self.assertRaises(ValueError, io.FileIO, TESTFN, 'x')

    def test_invalid_fd(self):
        self.assertRaises(ValueError, io.FileIO, -10)
        self.assertRaises(Value
