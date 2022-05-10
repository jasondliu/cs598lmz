import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# Test the codecs module

import codecs
import sys
import unittest
import warnings

class CodecsModuleTest(unittest.TestCase):

    def test_aliases(self):
        # Test the codec aliases
        self.assertEqual(codecs.lookup('string_escape'),
                         codecs.lookup('string-escape'))
        self.assertEqual(codecs.lookup('unicode_escape'),
                         codecs.lookup('unicode-escape'))
        self.assertEqual(codecs.lookup('raw_unicode_escape'),
                         codecs.lookup('raw-unicode-escape'))

    def test_utf7(self):
        # Test the UTF-7 codec
        self.assertEqual(codecs.utf_7_encode(u'\u20ac'),
                         ('+AOQ-', 5))
        self.assertEqual(codecs.utf_7_encode(u'\u20ac', 'strict'),
                         ('+AOQ-',
