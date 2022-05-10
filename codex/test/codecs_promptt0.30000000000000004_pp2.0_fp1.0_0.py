import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        def handler(exception):
            return ("test", exception.end)
        codecs.register_error("test.error", handler)
        self.assertEqual(codecs.lookup_error("test.error"), handler)
        self.assertRaises(LookupError, codecs.lookup_error, "test.error2")

    def test_register_error_twice(self):
        def handler(exception):
            return ("test", exception.end)
        codecs.register_error("test.error", handler)
        self.assertRaises(TypeError, codecs.register_error, "test.error", handler)

def test_main():
    test_support.run_unittest(TestRegisterError)

