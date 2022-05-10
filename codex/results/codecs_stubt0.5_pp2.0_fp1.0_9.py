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
    def test_ascii(self):
        self.assertEqual(codecs.ascii_decode("abc"), ("abc", 3))
        self.assertEqual(codecs.ascii_encode("abc"), ("abc", 3))

    def test_charmap(self):
        self.assertEqual(codecs.charmap_decode("abc"), ("abc", 3))
        self.assertEqual(codecs.charmap_encode("abc"), ("abc", 3))

    def test_utf_8(self):
        self.assertEqual(codecs.utf_8_decode("abc"), ("abc", 3))
        self.assertEqual(codecs.utf_8_encode("abc"), ("abc", 3))

    def test_utf_16(self):
        self.assertEqual(codecs.utf_16_decode("abc"), ("abc", 3))
        self.assertEqual(codecs.utf_
