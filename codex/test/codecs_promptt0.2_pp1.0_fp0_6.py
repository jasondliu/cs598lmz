import codecs
# Test codecs.register_error

# This test is not exhaustive, but it does test the most important
# features of the codecs module.

import codecs
import sys
import unittest

# Test the basic functionality of the codecs module

class CodecsModuleTest(unittest.TestCase):
    def test_aliases(self):
        self.assertEqual(codecs.lookup('utf-8'), codecs.lookup('utf_8'))
        self.assertEqual(codecs.lookup('utf-8'), codecs.lookup('UTF-8'))
        self.assertEqual(codecs.lookup('utf-8'), codecs.lookup('uTf-8'))
        self.assertEqual(codecs.lookup('utf-8'), codecs.lookup('UtF-8'))
        self.assertEqual(codecs.lookup('utf-8'), codecs.lookup('UTf-8'))
