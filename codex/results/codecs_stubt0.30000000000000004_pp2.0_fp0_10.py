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

    def test_utf8_errors(self):
        self.assertEqual(b"abc\xff".decode("utf-8", "strict"),
                         "\uFFFD")
        self.assertEqual(b"abc\xff".decode("utf-8", "replace"),
                         "abc\uFFFD")
        self.assertEqual(b"abc\xff".decode("utf-8", "ignore"),
                         "abc")
        self.assertEqual(b"abc\xc1".decode("utf-8", "strict"),
                         "\uFFFD")
        self.assertEqual(b"abc\xc1".decode("utf-8", "replace"),
                         "abc\uFFFD")
        self.assertEqual(b"abc\xc1".decode("utf-8", "ignore"),
                         "abc")
        self.assertEqual(b"abc\xff".decode("utf-8", "add_one_codepoint"),
                         "abca")

