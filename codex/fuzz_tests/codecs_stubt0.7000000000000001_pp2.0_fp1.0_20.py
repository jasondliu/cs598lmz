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

    def test_utf7(self):
        self.assertEqual(codecs.BOM_UTF7, b'+')
        self.assertEqual(codecs.BOM_UTF8, b'\xef\xbb\xbf')
        self.assertEqual(codecs.BOM_UTF16, b'\xff\xfe')
        self.assertEqual(codecs.BOM_UTF16_BE, b'\xfe\xff')
        self.assertEqual(codecs.BOM_UTF32, b'\xff\xfe\x00\x00')
        self.assertEqual(codecs.BOM_UTF32_BE, b'\x00\x00\xfe\xff')

        utf7 = codecs.getencoder('utf-7')
        utf7_be = codecs.getencoder('utf-7-be')
        utf7_imap = codecs.getencoder('utf-7-
