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
        # Test UTF-8
        self.assertEqual(codecs.utf_8_decode(b'\xff'), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x80'), (u'\u0000', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x81'), (u'\ufffd\u0001', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x81', 'replace'), (u'\ufffd\ufffd', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x81', 'ignore'), (u'\u0001', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc0\x81', 'back
