import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecRegressionTest(unittest.TestCase):

    def test_issue_5161(self):
        # This used to segfault
        self.assertRaises(TypeError, codecs.register_error, 'strict')

    def test_issue_5162(self):
        # This used to segfault
        self.assertRaises(TypeError, codecs.register_error, 42)

    def test_issue_5163(self):
        # This used to segfault
        self.assertRaises(TypeError, codecs.register_error, 'strict', 42)

    def test_issue_5164(self):
        # This used to segfault
        self.assertRaises(TypeError, codecs.register_error, 'strict', lambda x: x)

