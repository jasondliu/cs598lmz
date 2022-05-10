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
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='strict'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='replace'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='ignore'), ('\n', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors='add_one_codepoint'), ('a\xe9\n', 3))
        self.assertEqual(codecs
