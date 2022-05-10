import io
# Test io.RawIOBase and io.BufferedIOBase

import unittest
import io
from test import support
from io import BytesIO
# In 2.x, BytesIO is in the io module.  In 3.x, it's in the builtins.
try:
    from builtins import BytesIO
except:
    pass


class RawIOTest(unittest.TestCase):

    def test_read(self):
        b = bytes(range(256))
        for i in range(len(b)):
            for j in range(i, len(b)):
                rawio = io.BytesIO(b)
                self.assertEqual(rawio.read(i), b[:i])
                self.assertEqual(rawio.read(j), b[i:i+j])
                self.assertEqual(rawio.read(), b[i+j:])
                self.assertEqual(rawio.tell(), len(b))
                self.assertEqual(rawio.read(), b'')
                self.assertEqual(rawio.read
