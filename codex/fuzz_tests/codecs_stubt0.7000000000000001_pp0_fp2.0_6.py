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

class Unicode_test(unittest.TestCase):
    def test_classify(self):
        self.assertEqual(unicodedata.category(" "), 'Zs')
        self.assertEqual(unicodedata.category("A"), 'Lu')
        self.assertEqual(unicodedata.category("\uFFEE"), 'Cs')
        self.assertEqual(unicodedata.category("\U0001FFEE"), 'Cs')
        self.assertRaises(TypeError, unicodedata.category, b'A')
        self.assertRaises(TypeError, unicodedata.category, bytearray(b'A'))

    def test_lookup(self):
        self.assertEqual(unicodedata.lookup('LATIN CAPITAL LETTER A'), 'A')
        self.assertEqual(unicodedata.lookup('LATIN SMALL LETTER A'), 'a')
        self.assertEqual(unicodedata.lookup('\uFFEE'), '\uFFEE')
        self.assertEqual(unic
