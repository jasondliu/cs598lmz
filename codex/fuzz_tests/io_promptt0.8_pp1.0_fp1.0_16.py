import io
# Test io.RawIOBase and io.RawIOBase.readall()

import unittest
from test import support

class Readable(io.RawIOBase):
    def readable(self):
        return True

class Unseekable(Readable):
    def seekable(self):
        return False

class TestRawIOBase(unittest.TestCase):
    def test_readall(self):

        class SimpleRead(Readable):
            def readinto(self, buf):
                self.read_called = True
                return super().readinto(buf)

        # Test that readall() calls readinto() internally.
        s = SimpleRead()
        s.readall()
        self.assertTrue(s.read_called)

        # Test that if the object is seekable, the position is restored
        # after the operation.
        data = b'ABCDE'
        for n in range(len(data)):
            s = io.BytesIO(data)
            s.seek(n)
            self.assertEqual(s.tell(), n)
            self.assertEqual(
