import io
# Test io.RawIOBase.readinto() method

import unittest
from test.support import run_unittest


class BytesIOTest(unittest.TestCase):

    def test_readinto(self):
        import array
        b = io.BytesIO(b"abc")
        a = array.array('b', b"\0"*10)
        n = b.readinto(a)
        self.assertEqual(n, 3)
        self.assertEqual(a.tostring(), b"abc\0\0\0\0\0\0")


def test_main():
    run_unittest(BytesIOTest)


if __name__ == "__main__":
    test_main()
