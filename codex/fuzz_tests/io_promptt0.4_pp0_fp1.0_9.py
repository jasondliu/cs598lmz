import io
# Test io.RawIOBase

import _io

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:3] = b"foo"
                return 3
        buf = bytearray(5)
        f = TestRawIO()
        n = f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"foob\x00")
        n = f.readinto(buf)
        self.assertEqual(n, 0)
        self.assertEqual(buf, b"foob\x00")
        n = f.readinto(buf, 1)
        self.assertEqual(n, 0)
        self.assertEqual(buf, b"foob\x00")
        n = f.readinto(memoryview(buf)[1:4])
        self.
