import io
# Test io.RawIOBase.readall()

import unittest
from test import support


class RawIOTestCase(unittest.TestCase):

    def test_readall(self):
        # Per bug #1625426, calling readall() on a RawIO object that
        # was not opened in binary mode should raise an IOError.
        class RawIO(io.RawIOBase):
            def readinto(self, buf):
                return 0
            def read(self, n=-1):
                return b''
        self.assertRaises(IOError, RawIO().readall)

def test_main():
    support.run_unittest(RawIOTestCase)

if __name__ == '__main__':
    test_main()
