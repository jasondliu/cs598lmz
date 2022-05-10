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

class CodecsTestCase(unittest.TestCase):

    def setUp(self):
        self.test_text = 'abc\u20ac\u8abc\u10abc\u1000abc'

    def test_utf8(self):
        self.assertEqual(self.test_text.encode("utf-8"),
                         b'abc\xe2\x82\xac\xe8\x8a\xbc\xe1\x80\x8c\xe1\x80\x8c')
        self.assertEqual(self.test_text.encode("utf-8", "replace"),
                         b'abc\xe2\x82\xac\xe8\x8a\xbc?\xe1\x80\x8c?')
        self.assertEqual(self.test_text.encode("utf-8", "ignore"),
                         b'abc\xe2\x82\xac\xe8\x8a\xbc')
        self.assertEqual(self.test_text.encode("utf-
