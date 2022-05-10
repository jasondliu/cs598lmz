import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.my_error_handler', handler)
        self.assertEqual(codecs.lookup_error('test.my_error_handler'), handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.unknown_handler')
        self.assertRaises(TypeError, codecs.register_error, 'test.my_error_handler', None)
        self.assertRaises(TypeError, codecs.register_error, 'test.my_error_handler', 'spam')
        self.assertRaises(TypeError, codecs.register_error, 'test.my_error_handler', 42)
        self.assertRaises(TypeError, codecs.register_error, 'test.my_error_handler', object())
        self.assertRaises(TypeError
