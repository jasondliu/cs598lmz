import codecs
# Test codecs.register_error
from test import support

import unittest
from test import test_support

class ErrorTestCase(unittest.TestCase):
    def test_register_error(self):
        # Tests codecs.register_error
        #
        # This test is a bit weak, because it only tests the
        # registration part.  The error handling is tested in
        # test_codecs.

        def my_error_handler(exception):
            return ("spam", len(exception.object))

        def my_ignore_handler(exception):
            return ("", 1)

        def my_replace_handler(exception):
            return ("?", 1)

        def my_xmlcharrefreplace_handler(exception):
            return ("&#%d;" % (ord(exception.object[0]),), 1)

        def my_backslashreplace_handler(exception):
            return ("\\%d\\" % (ord(exception.object[0]),), 1)

        # This should work too
        codecs.register_error("my_ignore", my_
