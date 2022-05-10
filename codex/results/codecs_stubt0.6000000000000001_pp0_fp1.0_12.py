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

class TestUnicodeDecode(unittest.TestCase):
    def test_add_one_codepoint(self):
        b = b'\xa0'
        self.assertRaises(UnicodeDecodeError, b.decode, "ascii", "add_one_codepoint")
        self.assertEqual(b.decode("ascii", "add_one_codepoint"), 'a\xa0')
        self.assertRaises(UnicodeDecodeError, b.decode, "ascii", "add_utf16_bytes")
        self.assertRaises(UnicodeDecodeError, b.decode, "ascii", "add_utf32_bytes")
        self.assertRaises(UnicodeDecodeError, b.decode, "ascii", "ignore")

    def test_add_one_codepoint_2(self):
        b = b'\x80'
        self.assertRaises(UnicodeDecodeError, b.decode, "ascii", "
