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

    def test_utf8_bom(self):
        self.assertEqual(codecs.BOM_UTF8, b'\xef\xbb\xbf')
        self.assertEqual(codecs.BOM_UTF16, b'\xff\xfe')
        self.assertEqual(codecs.BOM_UTF16_BE, b'\xfe\xff')
        self.assertEqual(codecs.BOM_UTF32, b'\xff\xfe\x00\x00')
        self.assertEqual(codecs.BOM_UTF32_BE, b'\x00\x00\xfe\xff')

    def test_utf8_encoding(self):
        self.assertEqual(codecs.BOM_UTF8, b'\xef\xbb\xbf')
        self.assertEqual(codecs.BOM_UTF16, b'\xff\xfe')
        self.assertEqual(
