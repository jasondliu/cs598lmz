import io
# Test io.RawIOBase.readall()
import unittest

from test import support

class MockRawIO(io.RawIOBase):

    def readable(self):
        return True

    def seekable(self):
        return True

    def readinto(self):
        return 0

class Test(unittest.TestCase):

    def test_readall(self):
        # readall() calls seek(0); if that's not implemented, readall() isn't
        # either
        self.assertRaises(io.UnsupportedOperation, MockRawIO().readall)

def test_main():
    support.run_unittest(Test)
    support.reap_children()

if __name__ == "__main__":
    test_main()
