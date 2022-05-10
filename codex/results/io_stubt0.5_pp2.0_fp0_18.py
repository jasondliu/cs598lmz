import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# issue #15578
import _io
import io
import os
import sys
import tempfile
import unittest
import warnings

class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.fname = tempfile.mktemp()
        f = open(self.fname, "w")
        f.write("abcdefghijklmnopqrstuvwxyz\n")
        f.close()
        self.f = open(self.fname, "rb")

    def tearDown(self):
        self.f.close()
        os.remove(self.fname)

    def test_readinto(self):
        data = bytearray(b" " * 10)
        n = self.f.readinto(data)
        self.assertEqual(data, b"abcdefghij")
        self.assertEqual(n, 10)

    def test_readinto_array(self):
        from array import array
        data = array('b', b" " * 10)
        n
