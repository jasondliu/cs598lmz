import codecs
# Test codecs.register_error
import sys
import unittest

aacute = '\xc3\xa1'

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        def bad_handler(exception):
            raise exception
        codecs.register_error('test.bad', bad_handler)
        self.assertRaises(UnicodeError,
                          '%a'.__mod__, (aacute,))

        def bad2_handler(exception):
            raise SyntaxError
        codecs.register_error('test.bad2', bad2_handler)
        self.assertRaises(SyntaxError,
                          '%a'.__mod__, (aacute,))

    def test_lookup_error(self):
        self.assertEqual(codecs.lookup_error('strict'),
                         (UnicodeEncodeError, UnicodeDecodeError,
                          UnicodeTranslateError, ValueError))
