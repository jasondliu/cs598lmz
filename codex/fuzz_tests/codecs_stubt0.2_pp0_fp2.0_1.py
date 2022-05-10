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

class CodecsTest(unittest.TestCase):

    def test_utf8(self):
        self.assertEqual(codecs.decode("\xc3\x28", "utf-8", "replace"), "\ufffd(")
        self.assertEqual(codecs.decode("\xc3\x28", "utf-8", "ignore"), "")
        self.assertEqual(codecs.decode("\xc3\x28", "utf-8", "add_one_codepoint"), "a(")
        self.assertEqual(codecs.decode("\xc3\x28", "utf-8", "add_utf16_bytes"), "\udc00(")
        self.assertEqual(codecs.decode("\xc3\x28", "utf-8", "add_utf32_bytes"), "\x00\x00\x00(")
        self.assertEqual(codecs.decode("\xc3\x28", "utf-8", "strict"), None)

    def test
