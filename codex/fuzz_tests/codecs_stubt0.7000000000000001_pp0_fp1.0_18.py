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

class EncodingMapTest(unittest.TestCase):
    def setUp(self):
        self.encoding = "ascii"
        self.mapping = codecs.make_encoding_map(self.encoding)

    def test_encode_error(self):
        encoding = "ascii"
        mapping = codecs.make_encoding_map(self.encoding)
        self.assertRaises(UnicodeEncodeError,
            mapping.encode, "abc\xa0\xa1\xa2\xa3def", "replace")
        self.assertEqual(
            mapping.encode("abc\xa0\xa1\xa2\xa3def", "ignore"), b"abcdef")
        self.assertEqual(
            mapping.encode("abc\xa0\xa1\xa2\xa3def", "backslashreplace"),
            b"abc\\x00\\x01\\x02\\x03def")
        self.assertEqual(
            mapping.encode("abc\xa0\xa1\xa
