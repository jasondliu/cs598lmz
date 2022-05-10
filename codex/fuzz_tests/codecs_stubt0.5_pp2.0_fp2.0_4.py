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
    def test_attributes(self):
        exc = UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch")
        self.assertEqual(exc.encoding, "ascii")
        self.assertEqual(exc.object, b"\xff")
        self.assertEqual(exc.start, 1)
        self.assertEqual(exc.end, 2)
        self.assertEqual(exc.reason, "ouch")
        self.assertEqual(str(exc), "'ascii' codec can't decode byte 0xff in position 1: ouch")

        exc = UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch")
        self.assertEqual(exc.args, ("ascii", b"\xff", 1, 2, "ouch"))

    def test_start_pos(self):
        self.assertEqual(UnicodeDecodeError("ascii", b"\xff", 1, 2,
