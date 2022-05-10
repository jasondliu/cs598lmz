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
        # test utf-8 codec
        self.assertEqual(codecs.utf_8_encode("abc"), ("abc", 3))
        self.assertEqual(codecs.utf_8_encode("abc\xe4\xf6\xfc"), ("abc\xe4\xf6\xfc", 6))
        self.assertEqual(codecs.utf_8_encode("abc\xe4\xf6\xfc", 'strict'), ("abc\xe4\xf6\xfc", 6))
        self.assertEqual(codecs.utf_8_encode("abc\xe4\xf6\xfc", 'ignore'), ("abc", 3))
        self.assertEqual(codecs.utf_8_encode("abc\xe4\xf6\xfc", 'replace'), ("abc\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd", 9))
