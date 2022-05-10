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

class TestUTF8(unittest.TestCase):
    def test_utf8_decode(self):
        self.assertEqual("\u1234".encode("utf-8", "add_one_codepoint"), b'\xe1\x88\xb4')
        self.assertEqual("\u1234".encode("utf-8", "add_utf16_bytes"), b'\xe1\x88\xb4')
        self.assertEqual("\u1234".encode("utf-8", "add_utf32_bytes"), b'\xe1\x88\xb4')
        self.assertEqual("\u1234".encode("utf-8", "ignore"), b'')
        self.assertEqual("\u1234".encode("utf-8", "replace"), b'?')
        self.assertEqual("\u1234".encode("utf-8", "xmlcharrefreplace"), b'&#4660;')
        self.assertEqual("\u1234".encode("utf-8",
