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

from test import support

class StringTest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(TypeError, chr)
        self.assertRaises(TypeError, chr, 45, 45)
        self.assertRaises(ValueError, chr, sys.maxunicode + 1)
        self.assertRaises(ValueError, chr, -1)

    def test_len(self):
        self.assertEqual(1, len('a'))
        self.assertEqual(1, len('\u20ac'))
        self.assertEqual(1, len('\U0001d120'))

    def test_hash(self):
        self.assertRaises(TypeError, hash, 'a')

    def test_getitem(self):
        self.assertEqual('a', 'a'[0])
        self.assertRaises(IndexError, lambda: 'a'[1])
        self.assertRaises(TypeError, lambda: 'a'['a'])

    def test
