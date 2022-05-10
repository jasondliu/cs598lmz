import codecs
# Test codecs.register_error

import test.test_support
import unittest

class CodecsRegisterErrorTest(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error
        def bad_decode1(input, errors='strict'):
            raise UnicodeError, 'bad'
        def bad_encode1(input, errors='strict'):
            raise UnicodeError, 'bad'
        def bad_decode2(input, errors='strict'):
            raise UnicodeError, 'bad'
        def bad_encode2(input, errors='strict'):
            raise UnicodeError, 'bad'
        def bad_decode3(input, errors='strict'):
            raise UnicodeError, 'bad'
        def bad_encode3(input, errors='strict'):
            raise UnicodeError, 'bad'
        def bad_decode4(input, errors='strict'):
            raise UnicodeError, 'bad'
        def bad_encode4(input, errors='strict'):
            raise UnicodeError,
