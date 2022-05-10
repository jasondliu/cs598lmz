import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test registering and retrieving a custom error handler
        def custom_handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.custom', custom_handler)
        self.assertEqual(codecs.lookup_error('test.custom'), custom_handler)
        self.assertRaises(LookupError, codecs.lookup_error, '__builtin__')

    def test_register_error_invalid_args(self):
        # Test registering a custom error handler with invalid arguments
        self.assertRaises(TypeError, codecs.register_error)
        self.assertRaises(TypeError, codecs.register_error, 'test.custom')
        self.assertRaises(TypeError, codecs.register_error, 'test.custom',
                          lambda x: (u'', x.end), 42)
        self.assertRaises(TypeError
