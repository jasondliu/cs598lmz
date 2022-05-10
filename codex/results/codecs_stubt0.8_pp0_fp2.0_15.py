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

class EncodingTestCase(unittest.TestCase):

    def test_str_decode_error(self):

        def test_encoding(decode_err_handler):
            u = "abc\uDCFF"
            s = u.encode("utf-8", decode_err_handler)
            self.assertEqual(s, b"abc\xed\xb3\xbf")
            u = s.decode("utf-8", decode_err_handler)
            self.assertEqual(u, "abca")

        test_encoding("strict")
        test_encoding("ignore")
        test_encoding("replace")
        test_encoding(add_one_codepoint)

    def test_bytes_decode_error(self):

        def test_encoding(decode_err_handler):
            s = b"abc\xed\xb3\xbf"
            u = s.decode("utf-8", decode_err_handler)
            self.assertEqual(u, "abca")
            s
