import codecs
# Test codecs.register_error

# This test is derived from test_codecs.py

import codecs
import unittest

class CodecTest(unittest.TestCase):
    def test_register_error(self):
        # Test registering an error handler
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.myerrorhandler', handler)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'), handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.nosuchhandler')
        self.assertRaises(TypeError, codecs.register_error, 'test.myerrorhandler', 42)
        self.assertRaises(TypeError, codecs.register_error, 42, handler)

    def test_strict_errors(self):
        # Test strict error handler
        self.assertRaises(UnicodeDecodeError, 'abc'.decode, 'ascii', 'strict')
        self.assertRaises(UnicodeEn
