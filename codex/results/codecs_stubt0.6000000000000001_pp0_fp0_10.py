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

class TestUTF8(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(codecs.utf_8_decode(b'ab\xff', 'replace')[0],
                         'ab\ufffd')
        self.assertEqual(codecs.utf_8_decode(b'ab\xff', 'ignore')[0],
                         'ab')
        self.assertEqual(codecs.utf_8_decode(b'ab\xff', 'add_one_codepoint')[0],
                         'aba')
        self.assertEqual(codecs.utf_8_decode(b'ab\xff', 'add_utf16_bytes')[0],
                         'ab\ufffd')
        self.assertEqual(codecs.utf_8_decode(b'ab\xff', 'add_utf32_bytes')[0],
                         'ab\ufffd')

        self.assertEqual(codecs.utf_8_decode(b'ab\x80',
