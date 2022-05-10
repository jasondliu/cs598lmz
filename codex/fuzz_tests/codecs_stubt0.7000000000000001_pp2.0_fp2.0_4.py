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

class CodecTest(unittest.TestCase):
    def test_unicode_escape(self):
        if sys.maxunicode == 0xFFFF:
            self.assertEqual(u'\\Ufffffffe', codecs.unicode_escape_encode(u'\Ufffffffe')[0])
        else:
            self.assertEqual(u'\\U0010ffff', codecs.unicode_escape_encode(u'\U0010ffff')[0])

    def test_unicode_internal_encode(self):
        self.assertEqual(codecs.unicode_internal_encode(u'\u2603'), ('\x03\x02', 2))
        self.assertEqual(codecs.unicode_internal_encode(u'\U00020002'), ('\x02\x02\x02\x00', 4))

    def test_unicode_internal_decode(self):
        self.assertEqual(codecs.unicode_internal_decode('\x02\x02'), (
