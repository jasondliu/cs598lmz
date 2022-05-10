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

class CodecTest(unittest.TestCase):
    def test_utf8_decode(self):
        self.assertEqual(codecs.utf_8_decode(b'\x80'), (u'\u0080', 1))
        self.assertEqual(codecs.utf_8_decode(b'\x80', errors='strict'), (u'\u0080', 1))
        self.assertEqual(codecs.utf_8_decode(b'\x80', errors='ignore'), (u'', 1))
        self.assertEqual(codecs.utf_8_decode(b'\x80', errors='replace'), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\x80', errors='add_one_codepoint'), (u'a\u0080', 2))
        self.assertEqual(codecs.utf_8_decode(b'\x80', errors='add_utf16_bytes'), (
