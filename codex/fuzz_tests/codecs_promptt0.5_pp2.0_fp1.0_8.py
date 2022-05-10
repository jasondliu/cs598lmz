import codecs
# Test codecs.register_error()
import sys
import unittest
import encodings

class TestRegister(unittest.TestCase):
    def test_register(self):
        def bad_decode(input, errors='strict'):
            raise UnicodeDecodeError('bad_decode', input, 0, 1, 'test')
        def bad_encode(input, errors='strict'):
            raise UnicodeEncodeError('bad_encode', input, 0, 1, 'test')

        # Test that the error handler is called
        def handler(exception):
            self.assertEqual(exception.reason, 'bad_decode')
            self.assertEqual(exception.encoding, 'test')
            self.assertEqual(exception.start, 0)
            self.assertEqual(exception.end, 1)
            return (u'', exception.end)
        codecs.register_error('test', handler)
        self.assertEqual(b'abc'.decode('test', 'test'), u'abc')

        # Test that the error handler is called

