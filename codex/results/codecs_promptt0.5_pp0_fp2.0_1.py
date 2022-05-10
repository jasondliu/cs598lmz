import codecs
# Test codecs.register_error()

import codecs, codecs_test_support
import unittest

class Test_register_error(unittest.TestCase):
    # Test codecs.register_error()

    def test_lookup_error(self):
        # Test lookup of standard error handlers
        self.assertEqual(codecs.lookup_error('strict'), codecs.strict_errors)
        self.assertEqual(codecs.lookup_error('ignore'), codecs.ignore_errors)
        self.assertEqual(codecs.lookup_error('replace'), codecs.replace_errors)
        self.assertEqual(codecs.lookup_error('xmlcharrefreplace'),
                         codecs.xmlcharrefreplace_errors)
        self.assertEqual(codecs.lookup_error('backslashreplace'),
                         codecs.backslashreplace_errors)

    def test_register_error(self):
        # Test registration of new error handlers
        def my_errorhandler(exception):
            return ("my_errorhandler", exception
