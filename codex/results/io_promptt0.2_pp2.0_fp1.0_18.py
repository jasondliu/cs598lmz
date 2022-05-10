import io
# Test io.RawIOBase

import _io

class RawIOBaseTest(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        class TestRawIO(_io.RawIOBase):
            def __init__(self, buf):
                self.buf = buf
                self.pos = 0
            def readinto(self, b):
                n = len(b)
                if self.pos >= len(self.buf):
                    return None
                if n > len(self.buf) - self.pos:
                    n = len(self.buf) - self.pos
                b[:n] = self.buf[self.pos:self.pos+n]
                self.pos += n
                return n
            def readable(self):
                return True
        buf = bytearray(b"abcdefghij")
        f = TestRawIO(buf)
        b = bytearray(5)
        self.assertEqual(f.readinto(b), 5)
        self.assertEqual(b, buf[:5])
       
