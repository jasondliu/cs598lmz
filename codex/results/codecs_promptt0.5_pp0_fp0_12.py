import codecs
# Test codecs.register_error()

from test import support
from test.support import import_module

# Check that codecs.register_error() and 'replace' are available
codecs = import_module('codecs')

def run_error_callback_tests(self, encoding, test_string,
                             errorhandler, expected):
    encoded_string = test_string.encode(encoding)
    self.assertEqual(encoded_string.decode(encoding, errorhandler),
                     expected)
    self.assertEqual(encoded_string.decode(encoding, 'replace'),
                     expected)
    self.assertEqual(encoded_string.decode(encoding, 'ignore'),
                     expected)
    codecs.register_error(errorhandler, lambda x: None)
    self.assertEqual(encoded_string.decode(encoding, errorhandler),
                     expected)
    self.assertEqual(encoded_string.decode(encoding, 'replace'),
                     expected)
    self.assertEqual(encoded_string.decode(encoding
