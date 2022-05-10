import codecs
# Test codecs.register_error
from test import test_support
import unittest
from test.test_support import verbose, run_unittest
import warnings

class CodecRegistryTest(unittest.TestCase):
    def test_register_error(self):
        def bad_handler():
            pass
        self.assertRaises(TypeError, codecs.register_error, 'bad_handler',
                          bad_handler)
        self.assertRaises(TypeError, codecs.register_error, 'bad_handler',
                          codecs.strict_errors)
        self.assertRaises(TypeError, codecs.register_error, 'bad_handler',
                          codecs.ignore_errors)
        self.assertRaises(TypeError, codecs.register_error, 'bad_handler',
                          codecs.replace_errors)
        self.assertRaises(TypeError, codecs.register_error, 'bad_handler',
                          codecs.xmlcharrefreplace_errors)
        self.assertRaises(TypeError, codecs.register_error, 'bad_handler
