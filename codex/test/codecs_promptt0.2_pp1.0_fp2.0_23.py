import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Testing the register_error function
        def my_error_handler(exception):
            return ("my_handler", len(exception.object))

        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler)
        self.assertRaises(LookupError, codecs.lookup_error, "test.unknown")

        # Testing the register_error function with a tuple
        def my_error_handler1(exception):
            return ("my_handler1", len(exception.object))
        def my_error_handler2(exception):
            return ("my_handler2", len(exception.object))

