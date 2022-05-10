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
    def test_decode(self):
        self.assertEqual("abc", "abc".decode("utf-8"))
        self.assertEqual("abc", b"abc".decode("utf-8"))
        self.assertEqual("abc", bytearray(b"abc").decode("utf-8"))
        self.assertEqual("\u1234", b"\xe1\x88\xb4".decode("utf-8"))
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8", "strict")
        self.assertEqual("\ufffd", b"\xff".decode("utf-8", "replace"))
        self.assertEqual("\ufffd", b"\xff".decode("utf-8", "ignore"))
        self.assertEqual("\ufffd", b"\xff".decode("utf-8", "backslashreplace"))
        self.assertEqual("\ufffd", b"\
