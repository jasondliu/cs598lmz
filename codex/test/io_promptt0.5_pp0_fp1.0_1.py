import io
# Test io.RawIOBase.readall() method

import _io
import unittest

class TestRawIOBase(unittest.TestCase):

    def test_readall(self):
        # Issue #13704: io.RawIOBase.readall() should return an empty bytes
        # object when EOF is reached
        class RawIO(_io.RawIOBase):
            def readinto(self, buf):
                return 0
        r = RawIO()
        self.assertEqual(r.readall(), b'')


