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

class TestUNICODE(unittest.TestCase):
    def test_decode_line_too_short(self):
        line = b'\xfeU\xed\xa0'
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_be_decode, line)

    def test_decode_add_one(self):
        self.assertEqual(codecs.utf_16_be_decode(b'\xfeU\xed\xa0\x08', "replace", "add_one_codepoint"),
                (u'_\x08', 5))
        self.assertEqual(codecs.utf_16_be_decode(b'\xfeU\x80\x08', "replace", "add_one_codepoint"),
                (u'\ufffd\x08', 4))
        self.assertEqual(codecs.utf_16_be_decode(b'\xfeU\xed\xa0\x08\x0A', "replace
