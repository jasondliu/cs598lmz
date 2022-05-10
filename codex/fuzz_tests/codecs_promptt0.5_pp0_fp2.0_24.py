import codecs
# Test codecs.register_error()

import codecs
import unittest
from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering an error handler

        def bad_handler(exception):
            raise TypeError("bad error handler")

        codecs.register_error("test.bad_handler", bad_handler)
        self.assertRaises(TypeError, codecs.register_error,
                          "test.bad_handler", bad_handler)

        def replace_handler(exception):
            return ("?" * exception.end), exception.end + 1

        codecs.register_error("test.replace_handler", replace_handler)
        self.assertRaises(TypeError, codecs.register_error,
                          "test.replace_handler", replace_handler)

        def ignore_handler(exception):
            return ("", exception.end)

        codecs.register_error("test.ignore_handler", ignore_handler)
        self.assertRaises(TypeError, codecs.register_error,
                         
