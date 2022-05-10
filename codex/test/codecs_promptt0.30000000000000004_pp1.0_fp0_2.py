import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Testing codecs.register_error()
        def bad_handler(exception):
            return ("", exception.end)
        codecs.register_error("test.bad", bad_handler)
        self.assertEqual(codecs.lookup_error("test.bad"), bad_handler)
        self.assertRaises(LookupError, codecs.lookup_error, "test.unknown")
        codecs.register_error("test.bad", None)
        self.assertRaises(LookupError, codecs.lookup_error, "test.bad")
        self.assertRaises(TypeError, codecs.register_error, "test.bad", 1)
        self.assertRaises(TypeError, codecs.register_error, "test.bad", "foo")
        self.assertRaises(TypeError, codecs.register_error, "test.bad", "foo", "bar")
       
