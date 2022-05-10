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

###############################################################################

class CodecsTest(unittest.TestCase):

    def test_error_handling(self):
        text = "\u20ac400" # Euro symbol + a character that doesn't exist
        self.assertRaises(UnicodeEncodeError, text.encode, "ascii", "strict")
        self.assertEqual(text.encode("ascii", "add_one_codepoint"), b"a400")
        self.assertEqual(text.encode("ascii", "add_utf16_bytes"), b"ab")
        self.assertEqual(text.encode("ascii", "add_utf32_bytes"), b"abcd")

        data = b"\xe2\x82\xac400" # Euro symbol + garbage
        self.assertRaises(UnicodeDecodeError, data.decode, "ascii", "strict")
        self.assertEqual(data.decode("ascii", "add_one_codepoint"), "a400")
       
