import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error()
        def bad_decode(input, errors='strict'):
            raise UnicodeError
        def bad_encode(input, errors='strict'):
            raise UnicodeError
        codecs.register_error('test.notanencoding', bad_decode)
        codecs.register_error('test.notanencoding', bad_encode)
        self.assertRaises(UnicodeError,
                          '\xff'.decode, 'test.notanencoding')
        self.assertRaises(UnicodeError,
                          u'\u1234'.encode, 'test.notanencoding')

    def test_lookup_error(self):
        # Test codecs.lookup_error()
        def bad_decode(input, errors='strict'):
            raise UnicodeError
        def bad_encode(input, errors='st
