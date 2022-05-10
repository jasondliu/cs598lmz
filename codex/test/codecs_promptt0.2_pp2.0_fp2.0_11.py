import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error
        def bad_decode(input, errors='strict'):
            raise UnicodeError
        def bad_encode(input, errors='strict'):
            raise UnicodeError
        codecs.register_error('test.bad', bad_decode)
        codecs.register_error('test.bad', bad_encode)
        self.assertRaises(UnicodeError, codecs.lookup('ascii').decode, 'abc', 'test.bad')
        self.assertRaises(UnicodeError, codecs.lookup('ascii').encode, 'abc', 'test.bad')
        self.assertRaises(UnicodeError, codecs.lookup('ascii').decode, 'abc', 'test.bad')
