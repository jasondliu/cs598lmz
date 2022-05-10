import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_without_errorhandler(self):
        self.assertRaises(TypeError,
                          codecs.register_error,
                          'test_register_error', None)

    def test_register_duplicate_errorhandler(self):
        # Issue #13148: register_error() must not accept a name that is
        # already registered.
        #
        # Currently, the exception is silently swallowed.
        codecs.register_error('strict', codecs.strict_errors)
        self.assertRaises(TypeError,
                          codecs.register_error,
                          'strict', codecs.strict_errors)

    def test_lookup_errorhandler(self):
        # Issue #13149: lookup_error() must not accept a name that is
        # not registered.
        #
        # Currently, the function returns a wrapped error handler.
        self.assertRaises(TypeError,
                          codecs.lookup
