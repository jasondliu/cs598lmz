import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecsTest(unittest.TestCase):

    def test_register_error(self):
        def bad_handler(exception):
            raise TypeError
        self.assertRaises(TypeError, codecs.register_error, 'bad', bad_handler)

        def good_handler(exception):
            return (u'', exception.end)
        codecs.register_error('good', good_handler)
        self.assertEqual(codecs.lookup_error('good'), good_handler)
        codecs.register_error('good', None)
        self.assertRaises(LookupError, codecs.lookup_error, 'good')

        self.assertRaises(TypeError, codecs.register_error, 'good', good_handler, 42)
        self.assertRaises(TypeError, codecs.register_error, 'good', good_handler, 42, 42)
