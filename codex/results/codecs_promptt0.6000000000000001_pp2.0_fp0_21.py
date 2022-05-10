import codecs
# Test codecs.register_error
#
# This test is based on a test in the Python standard library.

import unittest
from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # This should be the default:
        self.assertEqual(codecs.lookup_error('strict'),
                         (UnicodeEncodeError, UnicodeDecodeError,
                          UnicodeTranslateError, ValueError))
        self.assertEqual(codecs.lookup_error('ignore'),
                         (None, None, None, None))

        def handler(exception):
            return ('', exception.end)

        codecs.register_error('test.ignore', handler)
        self.assertEqual(codecs.lookup_error('test.ignore'),
                         (handler, handler, handler, handler))
        self.assertEqual(codecs.lookup_error('test.strict'),
                         (UnicodeEncodeError, UnicodeDecodeError,
                          UnicodeTranslateError, ValueError))

        def handler(
