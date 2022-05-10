import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering a new error handler
        def my_handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.my_handler', my_handler)
        self.assertEqual(codecs.lookup_error('test.my_handler'), my_handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.unknown')
        # Test registering an existing error handler
        self.assertRaises(TypeError, codecs.register_error, 'test.my_handler',
                          my_handler)
        # Test registering an error handler with an invalid name
        self.assertRaises(TypeError, codecs.register_error, 'test', my_handler)
        self.assertRaises(TypeError, codecs.register_error, 'test.42',
                          my_handler)
        self.assertRaises(TypeError
