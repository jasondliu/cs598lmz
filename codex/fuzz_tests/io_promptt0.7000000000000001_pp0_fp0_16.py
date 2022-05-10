import io
# Test io.RawIOBase.readinto()
from io import RawIOBase
import unittest

from test.support import run_unittest
from test.support import bigmemtest

class RawIOTest(unittest.TestCase):
    def test_readinto(self):
        # Check readinto behaviour:
        # readinto() should always return an integer, even if it has less
        # bytes to return than available space in the buffer.
        # (This is the opposite of how read() works, since readinto() can
        # be used in a loop to read an unknown size object.)
        rawio = RawIOBase()
        try:
            rawio.readinto(bytearray(5))
        except OSError as e:
            self.assertEqual(e.errno, 22) # EINVAL
            # .readinto() should always return an int, even for an
            # empty buffer.
            self.assertTrue(rawio.readinto(bytearray(0)) is 0)
        else:
            self.fail("Calling .readinto() on an RawIO
