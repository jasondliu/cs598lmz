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

    def test_args(self):
        exc = UnicodeDecodeError("utf-8", b"\x80", 1, 2, "ouch")
        self.assertEqual(exc.encoding, "utf-8")
        self.assertEqual(exc.object, b"\x80")
        self.assertEqual(exc.start, 1)
        self.assertEqual(exc.end, 2)
        self.assertEqual(exc.reason, "ouch")
        self.assertEqual(str(exc), "'utf-8' codec can't decode byte 0x80 in position 1: ouch")

    def test_str(self):
        exc = UnicodeDecodeError("utf-8", b"\x80", 1, 2, "ouch")
        self.assertEqual(str(exc), "'utf-8' codec can't decode byte 0x80 in position 1: ouch")

    def test_str_without_reason(self):
        exc = UnicodeDecodeError("utf-
