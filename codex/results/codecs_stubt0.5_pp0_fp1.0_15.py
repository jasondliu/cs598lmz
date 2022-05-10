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

    def test_utf8_decode_error(self):
        self.assertEqual(codecs.utf_8_decode(b'\xff', "strict", True), (None, 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', "strict", False), (None, 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', "replace", True), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', "replace", False), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', "ignore", True), (u'', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xff', "ignore", False), (u'', 1))
        self.assertEqual(cod
