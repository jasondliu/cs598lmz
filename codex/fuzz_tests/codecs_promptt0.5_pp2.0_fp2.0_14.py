import codecs
# Test codecs.register_error()

import codecs
import unittest

def search_function(encoding):
    if encoding == 'test.unicode':
        return codecs.lookup('utf-8')
    return None

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # test registering an error handler
        codecs.register(search_function)
        self.assertRaises(UnicodeError, codecs.decode, b'\xff', 'test.unicode')
        codecs.register_error('test', lambda exc: (b'', exc.start + 1))
        self.assertEqual(codecs.decode(b'\xff', 'test.unicode'), (u'\ufffd', 1))

class TestRegisterError2(unittest.TestCase):
    def test_register_error2(self):
        # test registering an error handler
        codecs.register(search_function)
        self.assertRaises(UnicodeError, codecs.decode, b'\xff', 'test.
