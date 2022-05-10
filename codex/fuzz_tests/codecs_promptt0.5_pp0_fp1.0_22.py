import codecs
# Test codecs.register_error

import codecs
import unittest

class TestCodecsRegisterError(unittest.TestCase):

    def test_register_error(self):
        def err_handler(exception):
            raise TypeError
        codecs.register_error("test.my_error_handler", err_handler)
        self.assertRaises(TypeError, codecs.lookup_error("test.my_error_handler"), UnicodeDecodeError("ascii", b"\xff", 0, 1, "ouch"))
        codecs.register_error("test.my_error_handler", None)
        self.assertRaises(LookupError, codecs.lookup_error, "test.my_error_handler")

    def test_lookup_error(self):
        self.assertRaises(LookupError, codecs.lookup_error, "__not_existing_error_handler__")
        # Check that the default error handlers are registered
        for name in ("strict", "ignore", "replace", "xmlcharrefreplace", "backslashreplace"):
            codec
