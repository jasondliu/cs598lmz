import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test the abstract methods of RawIOBase
        io.RawIOBase()
        io.BufferedIOBase()
        io.TextIOBase()

    def test_close_flushes(self):
        # Test that close() flushes
        class MyRawIO(io.RawIOBase):
            def readable(self):
                return True
            def writable(self):
                return True
            def seekable(self):
                return True
            def readinto(self, b):
                raise OSError
            def write(self, b):
                self.b = b
                return len(b)
            def seek(self, pos, whence=0):
                pass
            def tell(self):
                return 0
            def flush(self):
                self.flushed = True
        r = MyRawIO()
        r.write(b"abc")
        self.assertFalse
