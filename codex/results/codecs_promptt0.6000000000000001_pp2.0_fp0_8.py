import codecs
# Test codecs.register_error()
import tempfile
import unittest
from test import support

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def my_error_handler(exception):
            return ("", exception.end)

        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler)
        codecs.register_error("test.my_error_handler", None)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"), None)

    def test_register_error_invalid_name(self):
        # Check that we get a sensible error message when registering a
        # codec with an invalid name.
        self.assertRaisesRegex(TypeError,
                               "codec_name must be a string",
                               codecs.register_error, None)
        self.assertRaisesRegex(TypeError,
                
