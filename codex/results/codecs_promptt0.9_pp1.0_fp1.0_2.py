import codecs
# Test codecs.register_error() function.

# -*- encoding: utf-8 -*-

import unittest
from test import test_support
import codecs
import sys

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error("ignore", 42))
        self.assertRaises(TypeError, codecs.register_error("ignore", lambda:None, 42))

        def illegal_errorhandler(exception):
            raise RuntimeError("This error handler cannot be called")

        self.assertRaises(RuntimeError, codecs.register_error("ignore", illegal_errorhandler))

        def errorhandler(exception):
            if not isinstance(exception, UnicodeEncodeError):
                raise RuntimeError("This error handler can only handle UnicodeEncodeError")

        codecs.register_error("illegalencode", errorhandler)
        self.assertEqual(codecs.lookup_error("illegalencode"),
                         (errorhandler, 'strict', UnicodeEncodeError))

       
