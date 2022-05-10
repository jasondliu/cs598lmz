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

class CodecsTest(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(codecs.escape_decode(b'abc'), (b'abc', 3))
        self.assertEqual(codecs.escape_decode(b'abc', errors='strict'),
                         (b'abc', 3))
        self.assertEqual(codecs.escape_decode(b'abc\\'), (b'abc\\', 4))
        self.assertRaises(UnicodeDecodeError, codecs.escape_decode,
                          b'abc\\x', errors='strict')
        self.assertRaises(UnicodeDecodeError, codecs.escape_decode,
                          b'abc\\x', errors='strict')
        self.assertEqual(codecs.escape_decode(b'abc\\x', errors='replace'),
                         (b'abc?', 4))
        self.assertEqual(codecs.escape_decode(b'abc\\x', errors='ignore'),
