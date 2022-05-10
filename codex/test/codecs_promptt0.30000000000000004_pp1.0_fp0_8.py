import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error
        def g(exception):
            return (u'', 0)
        codecs.register_error('test.g', g)
        self.assertEqual(codecs.lookup_error('test.g'), g)
        self.assertRaises(TypeError, codecs.register_error, 'test.g', 0)
        self.assertRaises(TypeError, codecs.register_error, 'test.g', None)
        self.assertRaises(TypeError, codecs.register_error, 'test.g', 'spam')
        self.assertRaises(TypeError, codecs.register_error, 'test.g', lambda: None)
        self.assertRaises(TypeError, codecs.register_error, 'test.g', lambda x: None)
