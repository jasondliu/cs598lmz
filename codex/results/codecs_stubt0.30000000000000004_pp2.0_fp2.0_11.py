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
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='strict'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='ignore'), ('\n', 0))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='replace'), ('\xe9\ufffd', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='add_one_codepoint'), ('\xe9a\n', 2))
        self.assertEqual(codecs.utf
