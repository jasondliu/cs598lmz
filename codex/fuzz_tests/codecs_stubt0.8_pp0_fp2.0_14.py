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

class UTF32Test(unittest.TestCase):

    def test_illegal_surrogate(self):
        error_handler = codecs.lookup_error("add_one_codepoint")
        d = codecs.getdecoder("utf-32")
        self.assertRaises(UnicodeDecodeError, d, b'\x00\x00\xdc\x00', 'strict')
        self.assertEqual(d(b'\x00\x00\xdc\x00', error_handler), ('a', 4))

        e = codecs.getencoder("utf-32")
        self.assertRaises(UnicodeEncodeError, e, '\udc00', 'strict')
        self.assertEqual(e('\udc00', error_handler), (b'a', 1))

    def test_illegal_surrogate_in_codec_search_function(self):
        error_handler = codecs.lookup_error("add_one_codepoint")
        self.assertRaises(Un
