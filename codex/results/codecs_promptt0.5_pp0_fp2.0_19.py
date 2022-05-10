import codecs
# Test codecs.register_error
#
# This test was written to verify that codecs.register_error()
# works as advertised.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
# Modified by Martin v. Loewis.

from test import test_support
import unittest
import codecs

def search_function(encoding):
    # The 'search' function is called by the codecs module to find
    # an appropriate codec.
    if encoding == 'test.unicode.replace':
        return codecs.lookup('unicode_internal')
    return None

class Test_Register_Error(unittest.TestCase):

    def test_replace(self):
        # Test the 'replace' error handler
        self.assertEqual(u'\ufffd'.encode('ascii', 'replace'), '?')
        self.assertEqual(u'\ufffd'.encode('ascii', 'replace'), '?')
        self.assertEqual(u'\ufffd'.encode('ascii', 'replace'), '?')

   
