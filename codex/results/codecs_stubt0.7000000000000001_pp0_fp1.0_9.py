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

class CodecTest(unittest.TestCase):
    def test_bad_utf8(self):
        # Issue #1558
        self.assertEqual(b"\xed\xa0\x80".decode("utf-8", "replace"), u"\ufffd")
        self.assertEqual(b"\xed\xa0\x80\xed\xb0\x80".decode("utf-8", "replace"),
                                         u"\ufffd\ufffd")
        self.assertEqual(b"\xed\xa0\x80".decode("utf-8", "ignore"), u"")
        self.assertEqual(b"\xed\xa0\x80\xed\xb0\x80".decode("utf-8", "ignore"), u"")
        self.assertEqual(b"\xed\xa0\x80".decode("utf-8", "add_one_codepoint"), u"\ufffd")
        self.assertEqual(b"\xed\xa0\x80
