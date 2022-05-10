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

class ErrorHandlingTest(unittest.TestCase):

    def test_decode_error_handling(self):
        self.assertEqual("abc\ufffd", "abc\u1234".decode("ascii", "add_one_codepoint"))

    def test_encode_error_handling(self):
        self.assertEqual("abc".encode("ascii", "add_one_codepoint"), b"abc\x61")

    def test_lookup_error_handling(self):
        self.assertEqual("a", "\u1234".encode("ascii", "add_one_codepoint").decode("ascii"))
        self.assertEqual("a", "\u1234".encode("utf32", "add_utf32_bytes").decode("utf32"))

    def test_unicode_encode_error_handling(self):
        self.assertEqual("\udc00".encode("utf-16-le", "add_utf16_bytes"), b"\x00
