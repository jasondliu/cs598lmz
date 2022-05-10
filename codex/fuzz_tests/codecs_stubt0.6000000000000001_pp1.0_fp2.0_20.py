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

class TestCodecs(unittest.TestCase):
    def test_utf8(self):
        self.assertEqual(codecs.decode("\xc3\xa9", "utf-8"), "\u00e9")
        self.assertEqual(codecs.decode("\xc3\xa9", "utf-8", "strict"), "\u00e9")
        self.assertEqual(codecs.decode("\xc3\xa9", "utf-8", "replace"), "\u00e9")
        self.assertEqual(codecs.decode("\xc3\xa9", "utf-8", "xmlcharrefreplace"), "&#233;")
        self.assertEqual(codecs.decode("\xc3\xa9", "utf-8", "ignore"), "")
        self.assertEqual(codecs.decode("\xc3\xa9", "utf-8", "backslashreplace"), "\\u00e9")
        self.assertEqual(codecs.dec
