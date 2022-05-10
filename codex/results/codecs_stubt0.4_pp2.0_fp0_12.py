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
        self.assertEqual(b"\xc3\x28".decode("utf-8", "surrogateescape"),
                         b"\x1a".decode("latin-1"))
        self.assertEqual(b"\xc3\x28".decode("utf-8", "replace"), "\ufffd(")
        self.assertEqual(b"\xc3\x28".decode("utf-8", "ignore"), "")
        self.assertEqual(b"\xc3\x28".decode("utf-8", "backslashreplace"), "\\x1a")
        self.assertEqual(b"\xc3\x28".decode("utf-8", "xmlcharrefreplace"), "&#x1a;")
        self.assertEqual(b"\xc3\x28".decode("utf-8", "namereplace"), "\N{REPLACEMENT CHARACTER}(")
        self.assert
