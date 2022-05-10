import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.strict', handler)
        self.assertEqual(codecs.lookup_error('test.strict'), handler)
        codecs.register_error('test.strict', None)
        self.assertEqual(codecs.lookup_error('test.strict'), None)
        self.assertRaises(TypeError, codecs.register_error, 'test.strict',
                          'spam')
        self.assertRaises(TypeError, codecs.register_error, 'test.strict',
                          handler, 42)
        self.assertRaises(TypeError, codecs.register_error, 'test.strict',
                          handler, 42, 42)
