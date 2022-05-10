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
    def test_decode_error(self):
        self.assertTrue(issubclass(UnicodeDecodeError, ValueError))
        self.assertTrue(issubclass(UnicodeEncodeError, ValueError))
        self.assertTrue(issubclass(UnicodeTranslateError, ValueError))

        # test attributes
        u = UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch")
        self.assertEqual(u.encoding, "ascii")
        self.assertEqual(u.object, b"\xff")
        self.assertEqual(u.start, 1)
        self.assertEqual(u.end, 2)
        self.assertEqual(u.reason, "ouch")
        self.assertEqual(str(u), "'ascii' codec can't decode byte 0xff in position 1: ouch")

        u = UnicodeDecodeError("ascii", b"\xff", 1, 2, "
