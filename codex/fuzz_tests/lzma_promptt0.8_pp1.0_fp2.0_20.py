import lzma
# Test LZMADecompressor stateful object.
import test.support
import unittest
from test.support import run_unittest
import io

class LZMAFileTestCase(unittest.TestCase):

    def test_invalid(self):
        self.assertRaises(ValueError, lzma.LZMAFile, filename='', mode='')
        self.assertRaises(TypeError, lzma.LZMAFile, filename=b'', mode='')
        self.assertRaises(ValueError, lzma.LZMAFile, filename='', mode='r')
        self.assertRaises(ValueError, lzma.LZMAFile, filename='', mode='w')
        self.assertRaises(ValueError, lzma.LZMAFile, filename='', mode='x')
        self.assertRaises(ValueError, lzma.LZMAFile, filename='', mode='a')
        self.assertRaises(ValueError, lzma.LZMAFile, filename='', mode='rb')
        self.assertRaises(ValueError
