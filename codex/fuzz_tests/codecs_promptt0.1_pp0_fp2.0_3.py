import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.strict', handler)
        self.assertEqual(codecs.lookup_error('test.strict'), handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.strict2')
        codecs.register_error('test.strict2', handler)
        self.assertEqual(codecs.lookup_error('test.strict2'), handler)
        codecs.register_error('test.strict', None)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.strict')
        self.assertEqual(codecs.lookup_error('test.strict2'), handler)
        codecs.register_error('test.strict2', None)
        self.assertRaises(
