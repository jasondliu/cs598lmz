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

#
# Test the UTF-7 codec

class Test_UTF7(unittest.TestCase):
    def test_utf7_encode(self):
        encode_check('"+A-AAB"', "\u0001\u0002\u0003", "utf-7")
        encode_check('"+A-AAB+A-AAB"', "\u0001\u0002\u0003\u0001\u0002\u0003", "utf-7")
        # \x00 is not valid in UTF-7
        self.assertRaises(UnicodeEncodeError, '\x00'.encode, 'utf-7')
        # U+0020 is allowed in UTF-7
        encode_check('"+A-A"', "\x20", "utf-7")
        # U+0021 is allowed in UTF-7
        encode_check('"+A-!"', "\x21", "utf-7")
        # U+0022 is not valid in UTF-7
        self.assertRaises(UnicodeEncodeError, '"
