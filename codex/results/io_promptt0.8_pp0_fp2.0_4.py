import io
# Test io.RawIOBase class
import unittest
# Test exceptions
import types
# Test type objects


class BytesIOTest(unittest.TestCase):

    def test_init(self):
        b = bytearray(b'1234567890abcdef')
        bio = io.BytesIO(b)
        self.assertEqual(bio.getvalue(), b)
        self.assertIs(type(bio.getvalue()), bytes)

        bio = io.BytesIO(b'1234567890')
        self.assertEqual(bio.getvalue(), b'1234567890')
        self.assertIs(type(bio.getvalue()), bytes)

        bio = io.BytesIO(memoryview(b'1234567890'))
        self.assertEqual(bio.getvalue(), b'1234567890')
        self.assertIs(type(bio.getvalue()), bytes)

        bio = io.BytesIO()
        self.assertEqual(bio.getvalue(), b'')
        self.assertIs(type(
