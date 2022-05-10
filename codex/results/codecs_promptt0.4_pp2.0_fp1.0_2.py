import codecs
# Test codecs.register_error()
import string
import sys
import unittest
from test import support

class Error(Exception):
    pass

class CodecRegressionTest(unittest.TestCase):

    def test_bug_813891(self):
        # bug 813891: Test for buffer interface
        f = codecs.lookup('rot-13')[3]
        self.assertRaises(TypeError, f, 42)
        self.assertRaises(TypeError, f, 'spam')
        self.assertRaises(TypeError, f, u'spam')
        self.assertRaises(TypeError, f, [])
        self.assertRaises(TypeError, f, ())
        self.assertRaises(TypeError, f, {})

    def test_bug_823353(self):
        # bug 823353: Test for string exceptions
        f = codecs.lookup('rot-13')[3]
        self.assertRaises(TypeError, f, 'spam', 'strict')
        self.assertRaises(TypeError, f
