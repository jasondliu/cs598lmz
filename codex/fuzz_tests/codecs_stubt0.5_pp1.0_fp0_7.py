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

    def test_utf8_decode_error(self):
        self.assertEqual(b'\xc3\x28'.decode("utf-8", "strict"),
                         u'\ufffd(')
        self.assertEqual(b'\xc3\x28'.decode("utf-8", "ignore"), u'')
        self.assertEqual(b'\xc3\x28'.decode("utf-8", "replace"), u'\ufffd')
        self.assertEqual(b'\xc3\x28'.decode("utf-8", "add_one_codepoint"),
                         u'a(')
        self.assertEqual(b'\xc3\x28'.decode("utf-8", "add_utf16_bytes"),
                         u'a\ufffd')
        self.assertEqual(b'\xc3\x28'.decode("utf-8", "add_utf32_bytes"),
                         u'a\ufffd')

    def
