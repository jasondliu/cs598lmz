import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def my_error_handler(exception):
            return (u'', exception.end)
        codecs.register_error('my_error', my_error_handler)
        self.assertEqual(codecs.lookup_error('my_error'), my_error_handler)
        self.assertRaises(TypeError, codecs.register_error, 'my_error', 'foo')
        self.assertRaises(TypeError, codecs.register_error, 'my_error', lambda: None)
        self.assertRaises(TypeError, codecs.register_error, 'my_error', lambda x: None)
        self.assertRaises(TypeError, codecs.register_error, 'my_error', lambda x, y, z: None)
        self.assertRaises(TypeError, codecs.register_error, 'my_error', lambda x, y, z, t: None)
