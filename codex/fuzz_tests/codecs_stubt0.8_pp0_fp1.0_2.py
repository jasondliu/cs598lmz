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

class CodecsTests(unittest.TestCase):

    def test_builtin(self):
        self.assertEqual(codecs.encode("\xff", "hex_codec"), b'0xff')
        self.assertEqual(codecs.encode("\xff", "hex_codec", "strict"),
                         b'0xff')
        self.assertRaises(TypeError, codecs.encode, b"bytes", "hex_codec")

    def test_utf_16_be(self):
        self.assertEqual(codecs.encode("\ud800", "utf-16-be"), b'\x00\xd8')
        self.assertEqual(codecs.encode("\udc00", "utf-16-be"), b'\x00\xdc')
        self.assertEqual(codecs.encode("\ud800", "utf-16-be", "strict"),
                                   b'\x00\xd8')
        self.assertEqual(codecs.en
