import io
# Test io.RawIOBase

import unittest
from test import support
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair, BufferedRandom
from io import TextIOWrapper, StringIO
from io import SEEK_SET, SEEK_CUR, SEEK_END

class BaseTestRawIO(object):

    def test_rawio_attributes(self):
        rawio = self.RawIOClass(self.FileIO(support.TESTFN, "wb"))
        self.assertEqual(rawio.mode, "wb")
        self.assertEqual(rawio.name, support.TESTFN)
        rawio.close()

    def test_read(self):
        rawio = self.RawIOClass(self.FileIO(support.TESTFN, "wb"))
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        rawio.close()

    def test_readinto(self):
        rawio = self.RawIOClass(self.FileIO(support.TESTFN, "wb"))
        self
