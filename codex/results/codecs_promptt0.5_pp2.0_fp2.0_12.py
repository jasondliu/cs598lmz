import codecs
# Test codecs.register_error()
import re
import sys
import unittest
import warnings
from test import support

# Test a few codecs
for encoding in ['rot_13', 'hex_codec', 'quopri_codec']:
    support.import_module(encoding, deprecated=True)

class CodecsModuleTest(unittest.TestCase):

    def test_aliases(self):
        # Check that all aliases are present
        for encoding in codecs.aliases.aliases.keys():
            try:
                codecs.lookup(encoding)
            except LookupError:
                self.fail("codec not found for alias %s" % encoding)

    def test_bz2_codec(self):
        # Issue #1202
        self.assertEqual(codecs.decode('\xf1\xf2\xf3\xf4\xf5', 'bz2_codec'),
                         '\xf1\xf2\xf3\xf4\xf5')

    def test_escape_decode(self):
        # Issue #1202
