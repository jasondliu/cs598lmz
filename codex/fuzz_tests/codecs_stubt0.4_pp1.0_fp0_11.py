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
        self.assertEqual(codecs.utf_8_decode(b'abc'), ('abc', 3))
        self.assertEqual(codecs.utf_8_decode(b'\xff'), ('\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x80'), ('\x80', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x80', final=True), ('', 0))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x80', final=False), ('\x80', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x80', errors='strict'), ('', 0))
        self.assertEqual(codecs.utf_8_decode(b'\xc0
