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

class TestEncode(unittest.TestCase):
    def test_encode_error_callback(self):
        self.assertEqual(u"abc".encode("ascii", "add_one_codepoint"), b"abc")
        self.assertEqual(u"abc".encode("ascii", "add_one_codepoint"), b"abc")
        self.assertEqual(u"a\u1234c".encode("ascii", "add_one_codepoint"), b"abc")
        self.assertEqual(u"a\u1234c".encode("ascii", "add_one_codepoint"), b"abc")

    def test_encode_error_callback_utf16(self):
        self.assertEqual(u"abc".encode("utf-16", "add_utf16_bytes"), b"\xff\xfea\x00b\x00c\x00")
        self.assertEqual(u"abc".encode("utf-16", "add_utf16_
