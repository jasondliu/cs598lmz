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

class TestUTF16(unittest.TestCase):

    def test_utf16_decode(self):
        # check decoding
        self.assertEqual("abc", "abc".encode("utf-16").decode("utf-16"))
        self.assertEqual("\U00010001", "\U00010001".encode("utf-16").decode("utf-16"))
        self.assertEqual("\U00020002", "\U00020002".encode("utf-16").decode("utf-16"))
        self.assertEqual("\U00030003", "\U00030003".encode("utf-16").decode("utf-16"))
        self.assertEqual("\U00040004", "\U00040004".encode("utf-16").decode("utf-16"))
        self.assertEqual("\U00050000", "\U00050000".encode("utf-16").decode("utf-16"))
        self.assertEqual("\U00060000", "\U00060000".encode("utf-16").dec
