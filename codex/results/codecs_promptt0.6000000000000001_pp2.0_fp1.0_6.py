import codecs
# Test codecs.register_error
import os
import sys
import unittest
import warnings
from test.support import TESTFN, TESTFN_UNICODE, captured_stdout, findfile, \
    run_unittest, unlink, rmtree
from test import test_support
# Skip test if _multibytecodec is not available.
test_support.import_module('_multibytecodec')
import _multibytecodec

class Test_MultibyteCodec(unittest.TestCase):
    def test_make_encoding_map(self):
        c = _multibytecodec.MultibyteCodec()
        self.assertEqual(c.make_encoding_map(b'123'), {49: 49, 50: 50, 51: 51})
        self.assertEqual(c.make_encoding_map(b'1234'), {49: 49, 50: 50, 51: 51, 52: 52})

    def test_make_decoding_map(self):
        c = _multibytecodec.Multib
