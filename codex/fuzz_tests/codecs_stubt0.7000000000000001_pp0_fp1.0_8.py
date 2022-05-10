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

class TestEncoders(unittest.TestCase):

    def test_utf_16_le_encode(self):
        s = "abc"
        expected = b"\xff\xfea\x00b\x00c\x00"
        self.assertEqual(s.encode("utf-16-le"), expected)
        self.assertEqual(s.encode("utf-16-le", "strict"), expected)

    def test_utf_16_le_encode_error(self):
        s = "abc\udcba"
        self.assertRaises(UnicodeEncodeError, s.encode, "utf-16-le")
        self.assertRaises(UnicodeEncodeError, s.encode, "utf-16-le", "strict")
        self.assertEqual(s.encode("utf-16-le", "ignore"), b"\xff\xfea\x00b\x00c\x00")
        self.assertEqual(s.encode("utf-16-le
