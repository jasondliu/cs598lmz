import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error
        self.assertRaises(LookupError, codecs.register_error, "undefined")

        def bad_handler(exception):
            raise SystemError

        self.assertRaises(TypeError, codecs.register_error, "bad_handler",
                          bad_handler)

        def bad_handler2(exception):
            return 42

        self.assertRaises(TypeError, codecs.register_error, "bad_handler2",
                          bad_handler2)

        def bad_handler3(exception):
            return 42, 42

        self.assertRaises(TypeError, codecs.register_error, "bad_handler3",
                          bad_handler3)

        def bad_handler4(exception):
            return 42, 42, 42

