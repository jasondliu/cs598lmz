import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecRegistryTest(unittest.TestCase):
    def test_register_error(self):
        def ignore_errors(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u'', exc.end)
            else:
                raise TypeError("don't know how to handle")

        codecs.register_error('test.ignore', ignore_errors)
        self.assertEqual(codecs.lookup_error('test.ignore'), ignore_errors)

    def test_register_error_bad_args(self):
        def bad_handler():
            return (u'', 0)

        self.assertRaises(TypeError,
                          codecs.register_error, bad_handler)
        self.assertRaises(TypeError,
                          codecs.register_error, 'test.bad', bad_handler)
        self.assertRaises(TypeError,
                          codecs.register_error, 'test.bad',
                          lambda: None)
        self.assertRaises
