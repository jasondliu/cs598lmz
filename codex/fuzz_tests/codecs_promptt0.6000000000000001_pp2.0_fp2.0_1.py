import codecs
# Test codecs.register_error
import re
import string
import sys
import unittest
# Test codecs.getreader/getwriter, and readline
import io

from test import support

class CodecsModuleTest(unittest.TestCase):

    def test_aliases(self):
        self.assertEqual(codecs.lookup('utf8').name, 'utf-8')

    def test_decode(self):
        self.assertEqual(codecs.decode(b'abc'), 'abc')
        self.assertEqual(codecs.decode(b'abc', 'ascii'), 'abc')
        self.assertRaises(TypeError, codecs.decode)
        # self.assertRaises(UnicodeDecodeError,
        #                   codecs.decode, b'\xff', 'ascii')

    def test_encode(self):
        self.assertEqual(codecs.encode('abc'), b'abc')
        self.assertEqual(codecs.encode('abc', 'ascii'), b'
