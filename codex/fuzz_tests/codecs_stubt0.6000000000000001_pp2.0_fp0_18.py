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

    def test_utf16_decode_errors(self):
        self.assertEqual("\uFFFD", codecs.utf_16_decode("\xff", "replace")[0])
        self.assertEqual("\uFFFD", codecs.utf_16_decode("\xff", "ignore")[0])
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, "\xff", "strict")
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, "\xff\xff\xff", "replace")
        self.assertEqual("\uFFFD", codecs.utf_16_decode("\xff\xff\xff", "ignore")[0])
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, "\xff\xff\xff", "strict")
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_
