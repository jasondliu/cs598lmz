import io
# Test io.RawIOBase

import io
import unittest

class TestRawIOBase(unittest.TestCase):

    def test_override_close(self):
        # Issue #11459: close() should not be overridable
        class MyRawIO(io.RawIOBase):
            def close(self):
                pass
        self.assertRaises(TypeError, MyRawIO)

    def test_override_readinto(self):
        # Issue #11459: readinto() should not be overridable
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return 0
        self.assertRaises(TypeError, MyRawIO)

class TestRawIO(unittest.TestCase):

    def test_read_write(self):
        # Test writing and reading back
        data = b"abcdefghijklmnop"
        f = io.BytesIO()
        f.write(data)
        f.seek(0)
        d = f.read(5)
        self.assertEqual(d, b
