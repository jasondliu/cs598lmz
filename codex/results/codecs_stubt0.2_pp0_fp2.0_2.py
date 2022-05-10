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
        # test utf-8
        self.assertEqual(codecs.utf_8_decode(b'\xc3\xa9\n'), ('\xe9\n', 2))
        self.assertEqual(codecs.utf_8_decode(b'ab\xc3\xa9\n'), ('ab\xe9\n', 4))
        self.assertEqual(codecs.utf_8_decode(b'a\xc3'), ('a', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc3', 'replace'), ('?', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc3', 'ignore'), ('', 1))
        self.assertEqual(codecs.utf_8_decode(b'\xc3', 'backslashreplace'),
                         ('\\uFFFD', 1))
        self.assert
