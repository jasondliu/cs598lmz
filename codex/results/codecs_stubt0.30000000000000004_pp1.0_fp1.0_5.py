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

class TestUTF7(unittest.TestCase):

    def test_utf7(self):
        self.assertEqual(codecs.utf_7_encode("abc"), ("abc", 3))
        self.assertEqual(codecs.utf_7_encode("abc", "strict", ""),
                         ("abc", 3))
        self.assertEqual(codecs.utf_7_encode("abc", "strict", None),
                         ("abc", 3))
        self.assertEqual(codecs.utf_7_encode("abc", "strict", "xyz"),
                         ("abc", 3))
        self.assertEqual(codecs.utf_7_encode("abc", "strict", "xyz"),
                         ("abc", 3))
        self.assertEqual(codecs.utf_7_encode("abc", "strict", ""),
                         ("abc", 3))
        self.assertEqual(codecs.utf_7_encode("abc", "strict", None),
                         ("abc
