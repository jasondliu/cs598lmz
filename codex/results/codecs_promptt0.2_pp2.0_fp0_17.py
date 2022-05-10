import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def my_error_handler(exception):
            return ("my_handler", exception.end)
        codecs.register_error("my_error_handler", my_error_handler)
        self.assertEqual(codecs.lookup_error("my_error_handler"),
                         my_error_handler)
        codecs.register_error("my_error_handler", None)
        self.assertEqual(codecs.lookup_error("my_error_handler"), None)

def test_main():
    test_support.run_unittest(TestRegisterError)

if __name__ == "__main__":
    test_main()
