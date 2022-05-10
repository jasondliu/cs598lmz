import io
# Test io.RawIOBase.readinto.

import io
import unittest
import array

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        b = io.BytesIO(b'abcdef')
        a = array.array('b', b'xxxxx')
        n = b.readinto(a)
        self.assertEqual(n, len(a))
        self.assertEqual(a.tobytes(), b'abcde')
        #
        b = io.BytesIO(b'abcdef')
        a = array.array('b', b'xxxxx')
        n = b.readinto(a, 1)
        self.assertEqual(n, len(a)-1)
        self.assertEqual(a.tobytes(), b'xbcde')
        #
        b = io.BytesIO(b'abcdef')
        a = array.array('b', b'xxxxx')
        n = b.readinto(a, 1, 2)
        self.assertEqual(n, 2)

