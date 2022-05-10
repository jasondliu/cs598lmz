import io
# Test io.RawIOBase by using StringIO as RawIOBase.
import StringIO as StringIO
import util
import unittest

# Needed to test seek() and tell().
class RawIOTest(unittest.TestCase):

    def test_init(self):
        buf = StringIO.StringIO()
        rio = io.RawIOBase(buf)
        self.assert_(rio.mode == None)
        self.assert_(rio.name == None)
        self.assert_(not rio.isatty())
        rio = io.RawIOBase(buf, 'a', 42, 42j)
        self.assert_(rio.mode == 'a')
        self.assert_(rio.name == 42)
        self.assert_(rio.isatty() == 42j)

    def test_read(self):
        buf = StringIO.StringIO('abc')
        rio = io.RawIOBase(buf)
        self.assertEqual(rio.read(), 'abc')
        buf = StringIO.StringIO('abc')
        rio = io.RawIOBase(buf
