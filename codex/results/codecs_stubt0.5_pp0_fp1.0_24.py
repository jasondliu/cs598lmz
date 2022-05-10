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

# This is a test for issue #16790
# See http://bugs.python.org/issue16790
class UTF8DecodeTest(unittest.TestCase):

    def test_utf8_decode(self):
        self.assertEqual(u"a\u0FFF".encode("utf-8", "add_one_codepoint"), b"a\xEF\xBF\xBF")
        self.assertEqual(u"a\u0FFF".encode("utf-16", "add_utf16_bytes"), b"\xFF\xFE\x61\x00\x00\xFF\xFF")
        self.assertEqual(u"a\u0FFF".encode("utf-32", "add_utf32_bytes"), b"\xFF\xFE\x00\x00\x61\x00\x00\x00\xFF\xFF\xFF\xFF")

class UTF16DecodeTest(unittest.TestCase):

    def test_utf16_decode(self
