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

class TestCodec(unittest.TestCase):
    def test_add_one_codepoint(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual("a\x80x", "x".encode("latin-1", "add_one_codepoint"))
        with self.assertWarns(DeprecationWarning):
            self.assertEqual("a\x80", b"\x88\x80".decode("unicode-escape", "add_one_codepoint"))

    def test_add_utf16_bytes(self):
        with self.assertRaisesRegex(UnicodeError, "^codec can't decode byte"):
            "x".encode("utf-16", "add_utf16_bytes")

    def test_add_utf32_bytes(self):
        with self.assertRaisesRegex(UnicodeError, "^codec can't decode byte"):
            "x".encode("utf-32", "add_utf32_bytes")


class
