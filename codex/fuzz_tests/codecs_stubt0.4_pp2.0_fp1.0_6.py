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

class TestDecode(unittest.TestCase):
    def test_utf16_decode(self):
        self.assertEqual(codecs.utf_16_decode(b'\xff\xfea\x00b\x00',
                                              final=False),
                         (u'a', 2))
        self.assertEqual(codecs.utf_16_decode(b'\xff\xfea\x00b\x00',
                                              final=True),
                         (u'ab', 4))
        self.assertEqual(codecs.utf_16_decode(b'\xff\xfea\x00b\x00', 'strict',
                                              final=False),
                         (u'a', 2))
        self.assertEqual(codecs.utf_16_decode(b'\xff\xfea\x00b\x00', 'strict',
                                              final=True),
                         (u'ab', 4))
        self.assertRaises(UnicodeDec
