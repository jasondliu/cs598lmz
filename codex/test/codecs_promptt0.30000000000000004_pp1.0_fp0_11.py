import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Encoding
        def search_function(encoding):
            if encoding == "test.searchfunction.encoding":
                return codecs.lookup("utf-8")
            raise LookupError(encoding)
        codecs.register_error("test.searchfunction.encoding", search_function)
        self.assertEqual(codecs.lookup_error("test.searchfunction.encoding"),
                         search_function)
        self.assertRaises(LookupError, codecs.lookup_error, "spam")
        # Decoding
        def search_function(encoding):
            if encoding == "test.searchfunction.decoding":
                return codecs.lookup("utf-8")
            raise LookupError(encoding)
        codecs.register_error("test.searchfunction.decoding", search_function)
