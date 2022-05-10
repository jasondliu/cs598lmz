import codecs
# Test codecs.register_error
try:
    from test.support import run_unittest
except ImportError:
    from test.test_support import run_unittest

import unittest

class ErrorHandlingTestCase(unittest.TestCase):
    def test_surrogateescape(self):
        # Check that surrogateescape error handler is available
        encoding = 'ascii'
        try:
            codecs.encode('\udc80', encoding, 'surrogateescape')
        except LookupError:
            self.skipTest('surrogateescape error handler not available')
        try:
            codecs.encode('\udc80', encoding, 'ignore')
        except LookupError:
            self.skipTest('ignore error handler not available')

        # Test that surrogates are escaped when 'surrogateescape' is used
        self.assertEqual(codecs.encode('\udc80', encoding, 'surrogateescape'),
                         b'\x80')
        self.assertEqual(codecs.decode(b'\x80', encoding,
