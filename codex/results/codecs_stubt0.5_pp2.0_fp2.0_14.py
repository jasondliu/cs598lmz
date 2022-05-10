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

codecs.register_error("strict", codecs.strict_errors)
codecs.register_error("ignore", codecs.ignore_errors)
codecs.register_error("replace", codecs.replace_errors)

class TestEncodings(unittest.TestCase):

    def test_utf_7(self):
        self.assertEqual("+ZeVnLIqe-", "a+ImIDkQ".decode("utf-7"))

    def test_utf_8(self):
        self.assertEqual("\xfc", "\xc3\xbc".decode("utf-8"))
        self.assertEqual("\u20ac", "\xe2\x82\xac".decode("utf-8"))

    def test_utf_16(self):
        self.assertEqual("\u20ac", "\xac\x20".decode("utf-16"))
        self.assertEqual("\u20ac", "\xac\x20\x00\x00".decode("utf-16"))
       
