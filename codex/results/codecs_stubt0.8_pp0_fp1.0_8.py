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

class CodecsTestCase(unittest.TestCase):

    def test_utf_16_be_decode(self):
        # test invalid BOM
        self.assertRaises(UnicodeError, '\xff\xfe'.decode, "utf-16-be")
        # test invalid data
        self.assertRaises(UnicodeError, '\x00\x61\x00\x00'.decode, "utf-16-be")

    def test_utf_16_be_decode_error(self):
        self.assertEqual('a\uFFFD\uFFFD'.encode('utf_16_be', 'add_one_codepoint'),
                         b'\x00a\x00\x00\x00')

    def test_utf_16_be_encode_error(self):
        self.assertRaises(UnicodeError, '\x00a\x00\x00\x00'.decode, "utf-16-be",
                          'add_utf16_bytes')

    def test_
