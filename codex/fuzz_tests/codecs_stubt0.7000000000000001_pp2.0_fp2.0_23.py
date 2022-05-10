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

class Test_UnicodeDecode:

    def test_decode(self):
        self.assertEqual("abc".decode("ascii"), "abc")
        self.assertRaises(UnicodeDecodeError, "abc".decode, "iso8859-1")
        self.assertEqual("abc".decode("iso8859-1", "replace"), "abc")
        self.assertEqual("abc".decode("iso8859-1", "replace"), "abc")
        self.assertEqual("abc".decode("iso8859-1", "ignore"), "abc")

    def test_decode_callback(self):
        # 'add_one_codepoint' replaces one character with one character
        self.assertEqual("abc\xff".decode("ascii", "add_one_codepoint"),
                         "abc\ufffd")
        self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "ascii",
                                               "backslashreplace")
        # 'add_utf
