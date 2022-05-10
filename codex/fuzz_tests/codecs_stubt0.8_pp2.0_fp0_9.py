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

import unittest

class StrTest(unittest.TestCase):
    def test_cp_errors(self):
        # unicode-escape and raw-unicode-escape use the same errors
        for encoding in 'unicode-escape', 'raw-unicode-escape':
            self.assertEqual(codecs.decode("\\", encoding), '\\')
            self.assertEqual(codecs.decode("\\x", encoding), '\\x')
            self.assertEqual(codecs.decode("\\xz", encoding), '\\xz')
            self.assertEqual(codecs.decode("\\xz", encoding, "ignore"), '')
            self.assertEqual(codecs.decode("\\xz", encoding, "replace"), '\ufffd')
            self.assertEqual(codecs.decode("\\a", encoding, "strict"), '\a')
            self.assertRaises(SyntaxError, codecs.decode, "\\a", encoding, "strict", "surrogateescape
