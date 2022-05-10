import codecs
# Test codecs.register_error
import sys
import unittest
from test import support

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error
        def bad_decode_errorhandler(exception):
            return ("", exception.end)
        def bad_encode_errorhandler(exception):
            return ("", exception.end)
        codecs.register_error("test.bad_decode", bad_decode_errorhandler)
        codecs.register_error("test.bad_encode", bad_encode_errorhandler)
        self.assertEqual(codecs.lookup_error("test.bad_decode"),
                         bad_decode_errorhandler)
        self.assertEqual(codecs.lookup_error("test.bad_encode"),
                         bad_encode_errorhandler)
        self.assertRaises(TypeError, codecs.register_error, "test.bad_decode",
                          None)
        self.assertRaises(TypeError, codecs
