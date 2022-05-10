import codecs
# Test codecs.register_error()
import encodings
import encodings.aliases
import encodings.utf_8
import encodings.iso8859_1
import encodings.ascii
import encodings.idna
import encodings.unicode_escape
import encodings.string_escape
import encodings.raw_unicode_escape
import encodings.latin_1
import encodings.mbcs
import encodings.cp437
import encodings.charmap
import encodings.punycode
import encodings.unicode_internal
import encodings.undefined

# Test Unicode codecs
#import encodings.unicode_escape_decode
#import encodings.raw_unicode_escape_decode
#import encodings.unicode_internal_decode

import sys
import unittest
import warnings
import gc

from test import test_support

class CodecTest(unittest.TestCase):

    def test_aliases(self):
        # Encoding names should be registered in both normal form
