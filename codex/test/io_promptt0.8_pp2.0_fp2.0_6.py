import io
# Test io.RawIOBase.readall()

import _io
import unittest

class TestRawIO(unittest.TestCase):
    def setUp(self):
        self.byteBuffer = bytearray(range(0,100))

    def test_readall(self):
        for i in range(1, 25):
            for j in range(0, 100, i):
                readLen = j

                testRb = io.BytesIO(self.byteBuffer)
                testRb.seek(0, 0)

                result = testRb.readall()
                self.assertEqual(result, self.byteBuffer)

                testRb.seek(0, 0)

                testRb.read(readLen)
                result = testRb.readall()
                self.assertEqual(result, self.byteBuffer[readLen:])

                testRb.seek(0, 0)

                testRb.read(j)
                result = testRb.readall()
                self.assertEqual(result, b'')

