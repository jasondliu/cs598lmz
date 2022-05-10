import codecs
# Test codecs.register_error.
# In Python 2.3, codecs.register_error() should be available.

import codecs
import re
import types
import unittest
from test import test_support

class CodecsBaseTest(unittest.TestCase):
    # XXX add tests for the other methods too

    def test_register_error(self):
        def bad_handler(exception):
            return (u'', exception.end)
        self.assertRaises(TypeError, codecs.register_error, bad_handler)

        def bad_handler(exception):
            return ('', '', '')
        self.assertRaises(TypeError, codecs.register_error, bad_handler)

        def bad_handler(exception):
            return ('', ())
        self.assertRaises(TypeError, codecs.register_error, bad_handler)

        def bad_handler(exception):
            return ('', 1.1)
        self.assertRaises(TypeError, codecs.register_error, bad_handler)

        def bad_handler(exception):
           
