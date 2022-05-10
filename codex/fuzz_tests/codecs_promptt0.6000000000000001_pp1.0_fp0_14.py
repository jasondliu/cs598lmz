import codecs
# Test codecs.register_error()

import test.test_support
import unittest

# Error handler that uses the codec's replacement character
def bad_decode_error_handler(exception):
    return (u'\ufffd', exception.end)

# Error handler that only eats characters
def bad_decode_error_handler_without_replacement(exception):
    return (u'', exception.end)

# Error handler that only eats characters
def bad_encode_error_handler(exception):
    return (u'', exception.end)

class CodecsTestCase(unittest.TestCase):
    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error, 42)
        self.assertRaises(LookupError, codecs.register_error, 'spam')
        self.assertRaises(TypeError, codecs.register_error, 'xmlcharrefreplace', 42)
        self.assertRaises(TypeError, codecs.register_error, 'ignore', lambda x: (u'', x.end))

