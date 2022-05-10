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

    def test_init(self):
        e = UnicodeDecodeError("utf8", b"\xff", 1, 2, "ouch")
        self.assertEqual(e.encoding, "utf8")
        self.assertEqual(e.object, b"\xff")
        self.assertEqual(e.start, 1)
        self.assertEqual(e.end, 2)
        self.assertEqual(e.reason, "ouch")
        self.assertEqual(str(e), "'utf8' codec can't decode byte 0xff in position 1: ouch")

    def test_start_end(self):
        e = UnicodeDecodeError("utf8", b"\xff", 1, 2, "ouch")
        self.assertEqual(e.start, 1)
        self.assertEqual(e.end, 2)
        e.start = 3
        e.end = 4
        self.assertEqual(e.start, 3)
        self.assertE
