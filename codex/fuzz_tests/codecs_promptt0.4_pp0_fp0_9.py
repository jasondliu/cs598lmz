import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def my_error_handler(exception):
            return "", exception.end

        codecs.register_error("test.my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler"),
                         my_error_handler)
        self.assertEqual(codecs.lookup_error("test.my_error_handler1"),
                         None)

        # Issue #10588
        for name in ("test.my_error_handler", "test.my_error_handler1"):
            with self.assertRaises(TypeError):
                codecs.register_error(name, 42)
            with self.assertRaises(TypeError):
                codecs.register_error(42, my_error_handler)


def test_main():
    test_support.run_unittest(TestRegisterError)

if __name
