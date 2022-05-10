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

class TestErrorHandlers(unittest.TestCase):

    def test_add_one_codepoint(self):
        self.assertEqual(u"\uFFFD\uFFFD".encode("utf-8", "add_one_codepoint"),
                         b"\xef\xbf\xbd\x61")
        self.assertEqual(u"\uFFFD".encode("utf-16", "add_one_codepoint"),
                         b"\xff\xfd\x00\x61")
        self.assertEqual(u"\uFFFD".encode("utf-32", "add_one_codepoint"),
                         b"\xff\xfd\x00\x00\x00\x61")

    def test_add_utf16_bytes(self):
        self.assertEqual(u"\uFFFD\uFFFD".encode("utf-8", "add_utf16_bytes"),
                         b"\xef\xbf\xbd\xef\xbf\xbd\x61
