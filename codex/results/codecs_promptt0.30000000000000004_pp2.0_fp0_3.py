import codecs
# Test codecs.register_error
#
# This test is designed to be run in a subprocess,
# so that the codecs module is reloaded.
#
# The codecs module caches the error handlers, so we need to reload
# the module to test the registration.

import codecs
import unittest

class CodecsRegisterErrorTest(unittest.TestCase):
    def test_register_error(self):
        # This should not raise an exception
        codecs.register_error("test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
        # This should raise a LookupError
        self.assertRaises(LookupError, codecs.register_error, "test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors)

    def test_lookup_error(self):
        # This should not raise an exception
        codecs.lookup_error("test.xmlcharrefreplace")
        # This should raise a LookupError
        self.assertRaises(LookupError, codecs.lookup_error, "test.nonexistent")

def test_main
