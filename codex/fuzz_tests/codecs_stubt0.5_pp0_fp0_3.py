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
    def test_utf8_surrogates(self):
        self.assertEqual(b"\xf0\x90\x80\x80".decode("utf-8", "surrogatepass"),
                         "\U00010000")
        self.assertEqual(b"\xf4\x8f\xbf\xbf".decode("utf-8", "surrogatepass"),
                         "\U0010ffff")

        self.assertRaises(UnicodeDecodeError,
                          b"\xf0\x90\x80".decode, "utf-8", "surrogatepass")
        self.assertRaises(UnicodeDecodeError,
                          b"\xf0\x90".decode, "utf-8", "surrogatepass")
        self.assertRaises(UnicodeDecodeError,
                          b"\xf0".decode, "utf-8", "surrogatepass")

        self.assertRaises(UnicodeDecodeError,

