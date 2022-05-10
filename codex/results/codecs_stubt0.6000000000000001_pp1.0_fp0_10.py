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

    def test_utf8(self):
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n', errors="strict"),
                         ("\u00e9\n", 3))
        self.assertEqual(codecs.utf_8_decode(b'ab\xe9\n', errors="strict"),
                         ("ab\u00e9\n", 4))
        self.assertEqual(codecs.utf_8_decode(b'ab\xc3xyz', errors="strict"),
                         ("ab\ufffdxyz", 3))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xc3\xc3', errors="strict"),
                         ("\uFFFD\uFFFD\uFFFD", 3))
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xc3\xc3', errors="replace"),
                        
