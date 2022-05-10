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

    def test_utf8(self):
        self.assertEqual(codecs.utf_8_decode(b'\xff'), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', 'strict'), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', 'ignore'), (u'', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', 'replace'), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', 'add_one_codepoint'), (u'a\ufffd', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xff', 'add_utf16_bytes'), (u'\ufffd', 1))
        self.assertEqual
