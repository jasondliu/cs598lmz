import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Issue #7195: registering an error handler twice should raise a
        # LookupError.
        codecs.register_error('test', lambda x: (x, 0))
        self.assertRaises(LookupError, codecs.register_error, 'test',
                          lambda x: (x, 0))
        # Issue #7195: registering an error handler twice should raise a
        # LookupError.
        codecs.register_error('test', lambda x: (x, 0))
        self.assertRaises(LookupError, codecs.register_error, 'test',
                          lambda x: (x, 0))
        # Issue #7195: registering an error handler twice should raise a
        # LookupError.
        codecs.register_error('test', lambda x: (x, 0))
