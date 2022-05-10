import codecs
# Test codecs.register_error()
import os
import unittest

from test import test_support

# Need a unicode string with non-BMP character for this test.
non_bmp_char = u'\U0001d120'

class CodecsErrorTestCase(unittest.TestCase):
    errors = ('ignore',
              'replace',
              'xmlcharrefreplace',
              'backslashreplace',
              'namereplace')

    def test_illegal_error_handler_value(self):
        # illegal error handler values should raise a LookupError
        self.assertRaises(LookupError, codecs.getencoder, "utf-8",
                          "foobar")
    def test_codecs_lookup_error(self):
        # a LookupError should be raised if the codec can't be found
        self.assertRaises(LookupError, codecs.getencoder, "foobar")
    def test_nonstandard_errors(self):
        # should be able to register non-standard error handlers
        def bad_handler(exception):
            raise Exception
