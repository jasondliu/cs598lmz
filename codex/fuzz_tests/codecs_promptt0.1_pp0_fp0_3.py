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
        self.assertRaises(TypeError, codecs.register_error, 'my_error', 42)
        self.assertRaises(TypeError, codecs.register_error, 42, my_error_handler)
        self.assertRaises(TypeError, codecs.register_error, 'my_error', lambda x: (u'', x.end))
        self.assertRaises(TypeError, codecs.register_error, 'my_error', lambda x: (u'', x.end, u''))
        self.assertRaises(TypeError, codecs.register_error, 'my_error', lambda x: (u'
