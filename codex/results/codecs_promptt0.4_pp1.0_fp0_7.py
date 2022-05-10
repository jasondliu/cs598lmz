import codecs
# Test codecs.register_error
import test.test_support
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test that the codecs.register_error() function works
        # as expected.
        self.assertRaises(TypeError, codecs.register_error)
        self.assertRaises(TypeError, codecs.register_error, 42)
        self.assertRaises(TypeError, codecs.register_error, "strict")
        self.assertRaises(TypeError, codecs.register_error, "strict", 42)
        self.assertRaises(TypeError, codecs.register_error, "strict",
                          lambda x: x)

        def replace_handler(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u'\ufffd', exc.end)
            raise TypeError("don't know how to handle %r" % exc)

        # Check that the handler is called
        codecs.register_error("test.codec_error_handler", replace_
