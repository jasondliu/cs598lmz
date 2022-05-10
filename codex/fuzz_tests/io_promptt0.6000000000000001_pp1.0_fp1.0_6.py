import io
# Test io.RawIOBase
from _io import BytesIO as _BytesIO
import unittest
from test import support


class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test RawIOBase derived class: read(), readinto()
        class TestRawIO(_RawIOBase):
            def __init__(self, bufsize):
                self._readbuf = b'x' * bufsize
                self._writebuf = bytearray(b'x' * bufsize)
                self._pos = 0

            def readable(self):
                return True

            def writable(self):
                return True

            def seekable(self):
                return True

            def seek(self, pos, whence=0):
                if whence == 0:
                    self._pos = pos
                elif whence == 1:
                    self._pos += pos
                elif whence == 2:
                    self._pos = len(self._readbuf) + pos
                return self._pos

            def tell(self):
                return self._pos

            def readinto(self, b):
