import codecs
# Test codecs.register_error

import sys
import unittest
from test import support

class TestRegisterError(unittest.TestCase):

    def test_lookup_error(self):
        # Test LookupError behavior
        # First, try unknown errors
        self.assertRaises(LookupError, codecs.lookup_error, 'spam')
        self.assertRaises(LookupError, codecs.lookup_error, 'xmlcharrefreplace')
        # Then standard ones
        codecs.lookup_error('strict')
        codecs.lookup_error('ignore')
        codecs.lookup_error('replace')
        if hasattr(codecs, 'xmlcharrefreplace_errors'):
            codecs.lookup_error('xmlcharrefreplace')

    def test_register_error(self):
        # Test registering errors
        def ignore_exc(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u'', exc.end)
            else:
                raise TypeError("don't know how to handle %r" % exc)
