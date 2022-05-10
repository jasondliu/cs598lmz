import codecs
# Test codecs.register_error

import codecs
import unittest

class CodecRegistryTest(unittest.TestCase):

    def test_register_error(self):
        def handler(exception):
            if isinstance(exception, UnicodeEncodeError):
                return (u'\ufffd', exception.end)
            elif isinstance(exception, UnicodeDecodeError):
                return (u'\ufffd', exception.end-1)
            else:
                raise TypeError("don't know how to handle %r" % exception)
        codecs.register_error('test.codec', handler)
        self.assertEqual(codecs.lookup_error('test.codec'), handler)
        self.assertEqual(codecs.lookup_error('test.codec'), handler)
        self.assertRaises(LookupError, codecs.lookup_error, '__test.codec')
        self.assertRaises(TypeError, codecs.register_error, 'test.codec', None)
        self.assertRaises(TypeError, codecs
