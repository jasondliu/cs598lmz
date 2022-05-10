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

class TestDecode(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEqual(b"\xf4\x8f\xbf\xbf".decode("utf-32-be", "add_one_codepoint"), "\U0010ffffa")
        self.assertEqual(b"\x8f\xbf\xbf\xf4".decode("utf-32-le", "add_one_codepoint"), "\U0010ffffa")
        self.assertEqual(b"\x00\x00\x10\xff".decode("utf-32", "add_one_codepoint"), "\U0010ffffa")
        self.assertEqual(b"\x00\x10\xff\x00".decode("utf-32", "add_one_codepoint"), "\U0010ffffa")

        self.assertEqual(b"\xdb\xff\xdf\xff".decode("utf-16-be", "add_one_codepoint"), "\U0010
