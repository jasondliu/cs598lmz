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

class TestUTF7(unittest.TestCase):

    def test_encode_decode_utf7(self):
        utf7_encoded = codecs.getencoder("utf-7")
        utf7_decoded = codecs.getdecoder("utf-7")
        self.assertEqual(utf7_decoded(utf7_encoded("abc")[0])[0], "abc")
        self.assertEqual(utf7_decoded(utf7_encoded("abc\u20ac")[0])[0], "abc\u20ac")
        self.assertEqual(utf7_decoded(utf7_encoded("abc\u20ac", "strict")[0])[0], "abc\u20ac")
        self.assertEqual(utf7_decoded(utf7_encoded("abc\u20ac", "replace")[0])[0], "abc?")
        self.assertEqual(utf7_decoded(utf7_encoded("abc\u20ac", "ignore")[0])[
