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
        codecs.register_error('test.bad', bad_decode)
        self.assertRaises(UnicodeError, '\xff'.decode, 'ascii', 'test.bad')
        codecs.register_error('test.bad', bad_encode)
        self.assertRaises(UnicodeError, u'\u1234'.encode, 'ascii', 'test.bad')

def test_main():
    test_support.run_unittest(CodecsModuleTest)

