import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def my_errorhandler(exception):
            return "foo", exception.end
        codecs.register_error("my_errorhandler", my_errorhandler)
        self.assertEqual("foo\x80\x81".decode("ascii", "my_errorhandler"),
                         "foo\ufffd\ufffd")
        codecs.register_error("my_errorhandler", None)

    def test_register_error_bad_handler(self):
        self.assertRaises(TypeError, codecs.register_error, "strict", None)
        self.assertRaises(TypeError, codecs.register_error, "strict", "foo")
        self.assertRaises(TypeError, codecs.register_error, "strict", lambda: None)
        self.assertRaises(TypeError, codecs.register_error, "strict", lambda x: None)
        self.assertRaises(
