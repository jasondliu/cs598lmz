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

    def test_utf8_decode(self):
        self.assertEqual(codecs.utf_8_decode(b'\x00'), (u'\x00', 1))
        self.assertEqual(codecs.utf_8_decode(b'\x7f'), (u'\x7f', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc2\x80'), (u'\x80', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xdf\xbf'), (u'\u07ff', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xe0\xa0\x80'), (u'\u0800', 3))
        self.assertEqual(codecs.utf_8_decode(b'\xef\xbf\xbf'), (u'\uffff', 3))

