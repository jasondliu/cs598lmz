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

class TestUTF8(unittest.TestCase):
    def test_to_utf8(self):
        # Test UTF-8 decoding
        self.assertEqual(utf8_decode(b'abc'), 'abc')
        self.assertEqual(utf8_decode(b'\xe4\xbd\xa0\xe5\xa5\xbd'), '你好')
        self.assertEqual(utf8_decode(b'\xf0\x90\x8c\xbc'), '𐌼')
        self.assertEqual(utf8_decode(b'\xff'), '\ufffd')
        self.assertEqual(utf8_decode(b'\xff'*2), '\ufffd'+'\ufffd')
        self.assertEqual(utf8_decode(b'\xff'*3), '\ufffd'+'\ufffd'+'\ufffd')
        self.assertEqual(utf8_decode(b'\xff'*4), '\ufffd'
