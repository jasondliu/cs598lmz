import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsTest(unittest.TestCase):

    def test_register_error(self):
        # Encoding
        self.assertRaises(LookupError, codecs.register_error, 'test.notfound')
        self.assertRaises(TypeError, codecs.register_error, 'test.lookup', None)
        self.assertRaises(TypeError, codecs.register_error, 'test.lookup', lambda x: None)
        self.assertRaises(TypeError, codecs.register_error, 'test.lookup', lambda x, y: None)
        self.assertRaises(TypeError, codecs.register_error, 'test.lookup', lambda x, y, z: None)
        self.assertRaises(TypeError, codecs.register_error, 'test.lookup', lambda x, y, z, t: None)
