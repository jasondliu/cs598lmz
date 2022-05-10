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

class Test_Unicode:
    def test_decode_error_handling(self):
        # test UnicodeDecodeError handling in PyUnicode_Decode()
        self.assertRaises(UnicodeDecodeError, "abc\xff".encode, "ascii", "strict")
        self.assertRaises(UnicodeDecodeError, "abc\xff".encode, "ascii", "replace")
        self.assertRaises(UnicodeDecodeError, "abc\xff".encode, "ascii", "ignore")
        self.assertRaises(UnicodeDecodeError, "abc\xff".encode, "ascii", "backslashreplace")
        self.assertRaises(UnicodeDecodeError, "abc\xff".encode, "ascii", "namereplace")
        self.assertRaises(UnicodeDecodeError, "abc\xff".encode, "ascii", "xmlcharrefreplace")
        self.assertRaises(UnicodeDecodeError, "abc\xff
