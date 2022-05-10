import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def my_error_handler(exception):
            return (u'', exception.end)
        codecs.register_error('my_error', my_error_handler)
        self.assertEqual(codecs.lookup_error('my_error'), my_error_handler)
        self.assertEqual(codecs.lookup_error('my_error'), my_error_handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'my_error2')
        self.assertRaises(TypeError, codecs.register_error, 'my_error2', 'spam')
        self.assertRaises(TypeError, codecs.register_error, 'my_error2', lambda: None)
        self.assertRaises(TypeError, codecs.register_error, 'my_error2', lambda x: None)
        self.assertRaises(TypeError, codec
