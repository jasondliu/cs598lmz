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

class TestUnicodeStrings(unittest.TestCase):

    def test_utf8(self):
        # UCS2 build
        if sys.maxunicode == 65535:
            self.assertEqual(codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf'),
                             (65535, 4))
            self.assertEqual(codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf', 'replace'),
                             (65533, 4))
            self.assertEqual(codecs.utf_8_decode(b'\xf4\x8f\xbf\xbf', 'ignore'),
                             (65535, 4))
            self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode,
                              b'\xf4\x8f\xbf\xbf', 'strict', True)
            self.assertEqual(codecs.utf_8_decode(b'\
