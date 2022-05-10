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

class TestUnicodeEncode(unittest.TestCase):
    def test_lone_surrogates(self):
        self.assertEqual(b'\xed\xa0\x80', "\ud800".encode("utf-8"))
        self.assertEqual(b'\xed\xa0\x80', "\ud800".encode("utf-8", "replace"))
        self.assertEqual(b'?', "\ud800".encode("ascii", "replace"))
        self.assertEqual(b'?', "\ud800".encode("ascii", "ignore"))

        self.assertEqual(b'\xed\xa0\x80', "\ud800".encode("utf-8", "add_one_codepoint"))
        self.assertEqual(b'?', "\ud800".encode("ascii", "add_one_codepoint"))

        self.assertEqual(b'\xed\xa0\x80', "\ud800".encode("utf-8", "add_utf16_bytes
