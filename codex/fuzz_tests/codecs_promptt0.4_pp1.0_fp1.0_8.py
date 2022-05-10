import codecs
# Test codecs.register_error()
import os
import sys
import unittest
from test import support

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # This test is mainly to check that the API is present
        self.assertRaises(LookupError, codecs.register_error, 'spam')
        self.assertRaises(LookupError, codecs.register_error, 'xmlcharrefreplace')
        self.assertRaises(LookupError, codecs.register_error, 'ignore')
        self.assertRaises(LookupError, codecs.register_error, 'replace')
        self.assertRaises(LookupError, codecs.register_error, 'backslashreplace')
        self.assertRaises(LookupError, codecs.register_error, 'namereplace')
        self.assertRaises(LookupError, codecs.register_error, 'surrogateescape')
        self.assertRaises(LookupError, codecs.register_error, 'surrogatepass')

        def handler(ex):
           
