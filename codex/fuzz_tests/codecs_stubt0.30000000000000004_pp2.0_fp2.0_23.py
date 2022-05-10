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
        e = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "ouch")
        self.assertEqual(e.encoding, "utf-8")
        self.assertEqual(e.object, b"\xff")
        self.assertEqual(e.start, 0)
        self.assertEqual(e.end, 1)
        self.assertEqual(e.reason, "ouch")

    def test_start_gt_end(self):
        self.assertRaises(ValueError, UnicodeDecodeError, "utf-8", b"", 1, 0, "ouch")

    def test_bad_args(self):
        self.assertRaises(TypeError, UnicodeDecodeError, "utf-8", b"", 0, 1, b"ouch")
        self.assertRaises(TypeError, UnicodeDecodeError, "utf-8", b"", 0, 1, 42)

    def test_str(self
