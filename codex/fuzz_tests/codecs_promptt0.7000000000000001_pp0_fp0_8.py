import codecs
# Test codecs.register_error()
import textwrap
import traceback
import sys
import re
import os
import unittest
from test import support

class CodecsModuleTest(unittest.TestCase):
    # This is by no means a complete test for the codecs module, but merely
    # a test for the additional functionality added to the codecs module.
    # The codec tests test the codecs module in detail.

    def test_getreader(self):
        self.assertRaises(TypeError, codecs.getreader, 1)
        self.assertRaises(TypeError, codecs.getreader, "unknown", "")
        self.assertRaises(TypeError, codecs.getreader, "unknown", None, None, None)
        self.assertRaises(LookupError, codecs.getreader, "__spam__")

        utf8 = codecs.getreader("utf-8")
        utf8 = codecs.getreader("utf-8")(BytesIO(b"\xc3\xa9"))
        self.assertEqual(utf8.read(), "\u00e
