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
        self.assertEqual("abc".encode("utf-8"), b'abc')
        self.assertEqual("abc".encode("utf-8", "strict"), b'abc')
        self.assertEqual("\u00E9".encode("utf-8"), b'\xc3\xa9')
        self.assertEqual("\u00E9".encode("utf-8", "strict"), b'\xc3\xa9')
        self.assertEqual("\u00E9".encode("utf-8", "ignore"), b'')
        self.assertEqual("\u00E9".encode("utf-8", "replace"), b'?\n')
        self.assertEqual("\u00E9".encode("utf-8", "add_one_codepoint"), b'a\n')
        self.assertEqual("\u00E9".encode("utf-8", "add_utf
