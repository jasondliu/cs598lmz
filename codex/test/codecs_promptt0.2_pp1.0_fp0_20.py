import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error
        def bad_decode(input, errors='strict'):
            raise UnicodeError
        def bad_encode(input, errors='strict'):
            raise UnicodeError
        codecs.register_error("test.notanencoding",
                              lambda e: (u"\ufffd", e.end))
        self.assertRaises(TypeError, codecs.register_error,
                          "test.notanencoding", None)
        self.assertRaises(TypeError, codecs.register_error,
                          "test.notanencoding", lambda e: None)
        self.assertRaises(TypeError, codecs.register_error,
                          "test.notanencoding", lambda e: ("", ""))
