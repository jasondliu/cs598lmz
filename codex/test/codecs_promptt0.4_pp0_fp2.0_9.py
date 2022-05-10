import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error()
        def handler(exception):
            return ("", exception.end)
        codecs.register_error("test.strict", handler)
        self.assertEqual(codecs.lookup_error("test.strict"), handler)
        codecs.register_error("test.strict", None)
        self.assertEqual(codecs.lookup_error("test.strict"), None)
        # This should not raise an exception
        codecs.register_error(None, None)

    def test_lookup_error(self):
        # Test codecs.lookup_error()
        self.assertEqual(codecs.lookup_error("__no_such_error_handler_here__"),
                         None)
        self.assertEqual(codecs.lookup_error(None), None)

