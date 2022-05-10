import codecs
# Test codecs.register_error

import codecs
import unittest
from test import test_support

class CodecRegistryTest(unittest.TestCase):

    def test_register_error(self):
        def bad_handler(exception):
            raise TypeError
        self.assertRaises(TypeError,
                          codecs.register_error,
                          "test.bad_handler", bad_handler)
        self.assertRaises(LookupError,
                          codecs.lookup_error,
                          "test.bad_handler")
        def good_handler(exception):
            return (u"", 1)
        codecs.register_error("test.good_handler", good_handler)
        self.assertEqual(codecs.lookup_error("test.good_handler"),
                         good_handler)

def test_main():
    test_support.run_unittest(CodecRegistryTest)

if __name__ == "__main__":
    test_main()
