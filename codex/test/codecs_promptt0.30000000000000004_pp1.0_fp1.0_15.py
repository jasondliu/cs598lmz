import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # This test is not exhaustive, but it does check that
        # the codecs module is functioning properly
        def bad_decode(input, errors='strict'):
            raise UnicodeError
        def bad_encode(input, errors='strict'):
            raise UnicodeError
        codecs.register_error('test.notanencoding', bad_encode)
        codecs.register_error('test.notadecoding', bad_decode)
        self.assertRaises(UnicodeError,
                          '\xff'.decode, 'test.notanencoding')
        self.assertRaises(UnicodeError,
                          '\xff'.encode, 'test.notadecoding')

def test_main():
    test_support.run_unittest(TestRegisterError)

