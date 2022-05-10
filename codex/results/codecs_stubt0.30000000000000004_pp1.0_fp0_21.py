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
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9'), ('\xe9', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9', errors='strict'), ('\xe9', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9', errors='replace'), ('\xe9', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9', errors='ignore'), ('', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9', errors='add_one_codepoint'), ('\xe9a', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9', errors='add
