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

class TestUtf16(unittest.TestCase):
    def test_utf16_decode_error(self):
        self.assertEqual(codecs.utf_16_decode(b'ab', 'strict', True),
                         (u"ab", 2))
        self.assertEqual(codecs.utf_16_decode(b'ab', 'replace', False),
                         (u"ab", 2))
        self.assertEqual(codecs.utf_16_decode(b'ab', 'replace', True),
                         (u"ab", 2))
        self.assertEqual(codecs.utf_16_decode(b'ab', 'ignore', True),
                         (u"", 2))
        self.assertEqual(codecs.utf_16_decode(b'ab', 'add_one_codepoint',
                                              True),
                         (u"\uFFFDab", 4))
        self.assertEqual(codecs.utf_16_decode(b'ab', 'add_
