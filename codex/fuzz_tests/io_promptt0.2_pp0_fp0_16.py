import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test that read() returns an empty bytes object on EOF
        class TestRawIO(_io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                return 0
        rawio = TestRawIO()
        self.assertEqual(rawio.read(1), b'')
        self.assertEqual(rawio.read(10), b'')
        self.assertEqual(rawio.read(), b'')

    def test_read_non_empty(self):
        # Test that read() returns an empty bytes object on EOF
        class TestRawIO(_io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                buf[:] = b'x'
                return 1
        rawio = TestRawIO()
        self.assertEqual(rawio.read(1), b'x')
        self.assertEqual(
