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

class TestUnicodeDecodeError(unittest.TestCase):
    def test_constructor(self):
        UnicodeDecodeError("test", b"abc", 1, 2, "reason")

    def test_attributes(self):
        e = UnicodeDecodeError("test", b"abc", 1, 2, "reason")
        self.assertEqual(e.encoding, "test")
        self.assertEqual(e.object, b"abc")
        self.assertEqual(e.start, 1)
        self.assertEqual(e.end, 2)
        self.assertEqual(e.reason, "reason")

    def test_str(self):
        e = UnicodeDecodeError("test", b"abc", 1, 2, "reason")
        self.assertEqual(str(e), "'test' codec can't decode byte 0x61: reason")

    def test_repr(self):
        e = UnicodeDecodeError("test", b"abc", 1, 2, "reason")
        self.assertEqual(repr(
