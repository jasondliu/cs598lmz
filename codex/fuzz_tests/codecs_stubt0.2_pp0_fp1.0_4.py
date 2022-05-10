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

class TestCodecs(unittest.TestCase):

    def test_utf8_decode(self):
        self.assertEqual("\u3042".encode("utf-8"), b"\xe3\x81\x82")
        self.assertEqual("\u3042".encode("utf-8", "replace"), b"?\xe3\x81\x82")
        self.assertEqual("\u3042".encode("utf-8", "backslashreplace"), b"\\u3042\xe3\x81\x82")
        self.assertEqual("\u3042".encode("utf-8", "xmlcharrefreplace"), b"&#12354;\xe3\x81\x82")
        self.assertEqual("\u3042".encode("utf-8", "surrogateescape"), b"\x1a\xe3\x81\x82")
        self.assertEqual("\u3042".encode("utf-8", "surrogatepass"), b"\x1a\
