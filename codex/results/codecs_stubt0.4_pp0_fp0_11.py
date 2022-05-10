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

class TestUnicodeDecode(unittest.TestCase):

    def test_add_one_codepoint(self):
        # Issue #20594: test that adding one codepoint works
        self.assertEqual(u"\u1234".encode("ascii", "add_one_codepoint"), "a\u1234")

    def test_add_utf16_bytes(self):
        # Issue #20594: test that adding 2 bytes works
        self.assertEqual(u"\u1234".encode("utf-16", "add_utf16_bytes"), b"ab\xff\xfe\x34\x12")

    def test_add_utf32_bytes(self):
        # Issue #20594: test that adding 4 bytes works
        self.assertEqual(u"\u1234".encode("utf-32", "add_utf32_bytes"), b"abcd\x00\x00\x00\x34\x12")

class TestUnicodeEncode(unittest.TestCase):


