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

    def test_utf8(self):
        u = "\u3042\u3044\u3046"
        b = b"\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86"
        self.assertEqual(u.encode("utf-8"), b)
        self.assertEqual(u.encode("utf-8", "strict"), b)
        self.assertEqual(b.decode("utf-8"), u)
        self.assertEqual(b.decode("utf-8", "strict"), u)

        b = b"\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xff"
        self.assertRaises(UnicodeDecodeError, b.decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, b.decode, "utf-8", "strict")
        self.assert
