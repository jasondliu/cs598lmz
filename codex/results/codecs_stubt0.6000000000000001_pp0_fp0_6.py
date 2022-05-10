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
    def test_encoding_map_type(self):
        self.assertIsInstance(codecs.encodings_map, dict)

    def test_aliases_map_type(self):
        self.assertIsInstance(codecs.aliases, dict)

    def test_aliases_map(self):
        self.assertEqual(codecs.aliases['utf-8'], 'utf_8')
        self.assertEqual(codecs.aliases['utf8'], 'utf_8')
        self.assertEqual(codecs.aliases['UTF-8'], 'utf_8')
        self.assertEqual(codecs.aliases['UTF8'], 'utf_8')
        self.assertEqual(codecs.aliases['UTF_8'], 'utf_8')

    def test_encode_decode(self):
        self.assertEqual(codecs.encode("abc"), b"abc")
        self.assertE
