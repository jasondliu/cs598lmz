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

# Test that the error handlers are called
class TestCodecs(unittest.TestCase):
    def test_add_one_codepoint_utf16(self):
        self.assertEqual(u"\ufffd\ufffd\ufffd",
                         u"abc".encode("utf-16", "add_one_codepoint"))

    def test_add_one_codepoint_utf32(self):
        self.assertEqual(u"\ufffd\ufffd\ufffd",
                         u"abc".encode("utf-32", "add_one_codepoint"))

    def test_add_utf16_bytes_utf16(self):
        self.assertEqual(u"\ufffd\ufffd\ufffd",
                         u"abc".encode("utf-16", "add_utf16_bytes"))

    def test_add_utf16_bytes_utf32(self):
        self.assertEqual(u"\ufffd\ufffd\ufffd",
                         u"abc".encode("utf-32", "add_
