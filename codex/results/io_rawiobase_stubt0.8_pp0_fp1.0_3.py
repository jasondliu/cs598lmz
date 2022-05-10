import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return

MyIOBase = io.RawIOBase
class File(MyIOBase):
    def read(self, n=-1):
        return

import math
math.degrees(math.pi)
math.degrees(math.pi*value)

var = value
del var

import os
os.uname()[0]

import subprocess
subprocess.call(['ls', '-l'])

import unittest
class FooTest(unittest.TestCase):
    def testFoo(self):
        self.assert_(True)

import zlib
zlib.compress(data)
zlib.crc32(data)
zlib.decompress(data)
zlib.decompressobj().decompress(data)
zlib.crc32(data)

import zipfile
zipfile.ZipFile(filename).open().read()

import sys
sys.getdefaultencoding()

import traceback
traceback.print_stack()

import scipy
