import codecs
# Test codecs.register_error
# Bug: http://bugs.python.org/issue1548894

import unittest
import codecs

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test that register_error() works as expected.
        def my_handler(exc):
            return "", exc.end
        codecs.register_error("my.error", my_handler)
        self.assertEqual(codecs.lookup_error("my.error"), my_handler)
        self.assertRaises(LookupError, codecs.lookup_error, "my.error.not.exist")

        # Test that register_error() raises a TypeError if the handler
        # is not a callable object.
        self.assertRaises(TypeError, codecs.register_error, "my.error", None)
        self.assertRaises(TypeError, codecs.register_error, "my.error", "")
        self.assertRaises(TypeError, codecs.register_error, "my.error", 1)
