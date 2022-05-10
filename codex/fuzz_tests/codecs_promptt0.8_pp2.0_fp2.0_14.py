import codecs
# Test codecs.register_error()
import os
import re
import sys
import pickle
import unittest
import weakref
from test import test_support
from cStringIO import StringIO

ENCODING = 'utf-7'
TESTSTRING = u"a\u2262\u0391."
TESTUNICODE = u"a\u2262\u0391."

class TestUTF7(unittest.TestCase):

    def setUp(self):
        self.theTestEncoding = 'utf-7'
        # use StringIO so we can reset the position to 0
        self.theTestString = StringIO(TESTSTRING.encode(ENCODING))
        self.theTestUnicode = TESTUNICODE
        self.theTestData = self.theTestString.read()

    def test_exceptions(self):
        # Check the set of exceptions thrown by the codec
        self.assertEquals(codecs.lookup_error('strict'),
                          LookupError)
        self.assertEquals(codecs.lookup_error('
