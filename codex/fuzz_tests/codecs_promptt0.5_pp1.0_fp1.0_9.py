import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

import sys

class Test_Register_Error(unittest.TestCase):
    def test_register_error(self):
        import codecs
        codecs.register_error('strict', codecs.ignore_errors)
        self.assertEqual(codecs.lookup_error('strict'), codecs.ignore_errors)
        self.assertRaises(LookupError, codecs.lookup_error, '__not_found__')
        self.assertRaises(TypeError, codecs.register_error, '__not_callable__', 'not callable')
        self.assertRaises(TypeError, codecs.register_error, '__not_callable__', '\u1234')
        self.assertRaises(TypeError, codecs.register_error, '__not_callable__', '\u1234'.encode('ascii'))
        self.assertRaises(TypeError, codecs.register_error, '__not_callable__', '\u1234'.
