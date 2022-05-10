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
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa4\xe2\x82\xac\xf0\x90\x8c\xbc', 'strict', True),
                         ('\xe4\u20ac\U00010cbc', 9))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa4\xe2\x82\xac\xf0\x90\x8c', 'strict', True),
                         ('\xe4\u20ac', 6))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa4\xe2', 'strict', True),
                         ('\xe4', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa4', 'strict', True),
                         ('\xe4', 2))
