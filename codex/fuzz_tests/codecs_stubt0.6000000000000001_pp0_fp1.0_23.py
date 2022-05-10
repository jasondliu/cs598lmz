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

class TestDecodingErrorHandling(unittest.TestCase):

    def test_add_one_codepoint(self):
        for codec in ["utf-8", "utf-16", "utf-32"]:
            self.assertEqual("a", codecs.decode("\x80", codec, "add_one_codepoint"))
            self.assertEqual("a", codecs.decode("\x80\x80\x80", codec, "add_one_codepoint"))

    def test_add_utf16_bytes(self):
        self.assertEqual("ab", codecs.decode("\x80\x80", "utf-16", "add_utf16_bytes"))
        self.assertEqual("ab", codecs.decode("\x80\x80\x80\x80", "utf-16", "add_utf16_bytes"))

    def test_add_utf32_bytes(self):
        self.assertEqual("abcd", codecs.decode("\x80\x80\x80\x
