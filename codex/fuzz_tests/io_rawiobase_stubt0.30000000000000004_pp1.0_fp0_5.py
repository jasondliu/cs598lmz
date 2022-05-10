import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def readable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def writable(self):
        return False

import os
import tempfile
import unittest
from test import support

class RawIOBaseTest(unittest.TestCase):

    def test_constructor(self):
        f = File(__file__)
        self.assertEqual(f.name, __file__)
        self.assertIsNone(f
