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

class CodecsModuleTest(unittest.TestCase):
    def test_charmap_encode_decode(self):
        self.assertEqual(codecs.charmap_encode('abc', {97: 65, 98: 66, 99: 67}),
                         (b'ABC', 3))
        self.assertEqual(codecs.charmap_encode('abc', {97: None, 98: 66, 99: 67}),
                         (b'BC', 2))
        self.assertEqual(codecs.charmap_encode('abc', {97: 65, 98: 66, 99: None}),
                         (b'AB', 2))
        self.assertEqual(codecs.charmap_encode('abc', {97: 65, 98: None, 99: None}),
                         (b'A', 1))
        self.assertEqual(codecs.charmap_encode('abc', {97: None, 98: None, 99: None}),
                         (b'', 0))
        self.
