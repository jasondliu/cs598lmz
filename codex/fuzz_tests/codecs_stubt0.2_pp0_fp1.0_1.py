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

    def test_utf8_decode(self):
        self.assertEqual("abc".encode("utf-8"), b'abc')
        self.assertEqual("\u20ac".encode("utf-8"), b'\xe2\x82\xac')
        self.assertEqual("\U0001d120".encode("utf-8"), b'\xf0\x9d\x84\xa0')

        self.assertEqual(b'abc'.decode("utf-8"), "abc")
        self.assertEqual(b'\xe2\x82\xac'.decode("utf-8"), "\u20ac")
        self.assertEqual(b'\xf0\x9d\x84\xa0'.decode("utf-8"), "\U0001d120")

        self.assertEqual(b'\xe2\x82'.decode("utf-8", "strict"), "\u20ac")
        self.assertEqual(b'\xe2
