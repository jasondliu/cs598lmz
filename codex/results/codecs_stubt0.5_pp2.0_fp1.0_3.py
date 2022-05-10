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
        self.assertEqual(b"\xc3\xa9\xc3\xa9", codecs.utf_8_encode("\xe9\xe9")[0])
        self.assertEqual(b"\xe9\xe9", codecs.utf_8_decode(b"\xc3\xa9\xc3\xa9")[0])
        self.assertEqual(b"\xc3\xa9\xc3\xa9", codecs.utf_8_encode("\xe9\xe9", "replace")[0])
        self.assertEqual(b"\xe9\xe9", codecs.utf_8_decode(b"\xc3\xa9\xc3\xa9", "replace")[0])
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b"\xc3\xa9\xc3\xa9\xc3", "replace")
       
