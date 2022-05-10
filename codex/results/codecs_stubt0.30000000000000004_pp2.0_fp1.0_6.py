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
        self.assertEqual(
            UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch"),
            UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch")
        )
        self.assertNotEqual(
            UnicodeDecodeError("ascii", b"\xff", 0, 2, "ouch"),
            UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch")
        )
        self.assertNotEqual(
            UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch"),
            UnicodeDecodeError("ascii", b"\xff", 1, 3, "ouch")
        )
        self.assertNotEqual(
            UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch"),
            UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouuch
