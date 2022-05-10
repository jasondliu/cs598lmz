import codecs
# Test codecs.register_error.
import pickle
import unittest
from test import test_support
from test.test_support import TESTFN
import os
import sys
import warnings


class Test_cp65001(unittest.TestCase):
    def test_surrogates(self):
        # Issue #11395
        self.assertRaises(UnicodeEncodeError, 'a\uD800b'.encode, 'cp65001')
        self.assertRaises(UnicodeDecodeError, 'a\x81b'.decode, 'cp65001')


class Test_cp1251(unittest.TestCase):
    def test_error_callback(self):
        def bad_decode_handler(exception):
            self.assertEqual(exception.start, 1)
            self.assertEqual(exception.end, 2)
            self.assertEqual(exception.object, '\x81')
            return (u'\uFFFD', exception.end)
        self.assertEqual('a\uFFFDb'.decode(
            '
