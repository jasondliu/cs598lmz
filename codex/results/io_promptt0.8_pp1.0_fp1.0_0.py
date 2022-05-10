import io
# Test io.RawIOBase, io.BytesIO and io.BufferedIOBase
# Derived from test_io, which is under PSF license
import unittest
import os
import stat
from test import support
from io import BytesIO, BufferedWriter, BufferedReader, BufferedRWPair, BufferedRandom
from io import DEFAULT_BUFFER_SIZE
import pickle
from io import UnsupportedOperation
from io import SEEK_CUR, SEEK_END, SEEK_SET
from io import BufferedIOBase, RawIOBase

MSG = b"a little message"

class BaseTest(object):

    def test_read(self):
        b = self.thetype(MSG)
        self.assertEqual(b.read(), MSG)

    def test_readinto(self):
        b = self.thetype(MSG)
        buf = bytearray(len(MSG) + 10)
        self.assertEqual(b.readinto(buf), len(MSG))
        self.assertEqual(buf[:len(MSG)], MSG)
       
