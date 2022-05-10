import codecs
# Test codecs.register_error

import codecs
import unittest

class ErrorTest(unittest.TestCase):
    def test_register(self):
        self.assertRaises(TypeError, codecs.register_error, "not callable")
        self.assertRaises(TypeError, codecs.register_error, lambda x: x, "not a string")
        self.assertRaises(LookupError, codecs.register_error, lambda x: x, "unknown")

def test_main():
    test_support.run_unittest(ErrorTest)

if __name__ == "__main__":
    test_main()
