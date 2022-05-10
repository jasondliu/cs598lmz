import codecs
# Test codecs.register_error

import test.test_support
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # This test fails if codecs.register_error is not present
        self.assert_(hasattr(codecs, "register_error"))

    def test_lookup_error(self):
        # This test fails if codecs.lookup_error is not present
        self.assert_(hasattr(codecs, "lookup_error"))

    def test_strict(self):
        # StrictError should be the default error handler
        self.assertEqual(codecs.lookup_error("strict"), codecs.strict_errors)

    def test_ignore(self):
        # Ignore should be a valid error handler
        self.assertEqual(codecs.lookup_error("ignore"), codecs.ignore_errors)

    def test_replace(self):
        # Replace should be a valid error handler
        self.assertEqual(codecs.lookup_error("replace"), codecs
