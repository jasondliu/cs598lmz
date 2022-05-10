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
    def test_utf8_decode(self):
        self.assertEqual(codecs.utf_8_decode(b'\xc3\x28', "replace")[0],
                         '\ufffd(')
        self.assertEqual(codecs.utf_8_decode(b'\xc3\x28', "ignore")[0],
                         '')
        self.assertEqual(codecs.utf_8_decode(b'\xc3\x28', "backslashreplace")[0],
                         '\\xc3\\x28')
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode, b'\xc3\x28', "strict")
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode, b'\xc3\x28', "xmlcharrefreplace")

        self.assertEqual(codecs.utf_8_
