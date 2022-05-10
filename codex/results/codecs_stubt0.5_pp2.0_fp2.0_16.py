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
    def test_add_one_codepoint(self):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            self.assertEqual(
                u'a\udc80'.encode(encoding, 'add_one_codepoint'),
                b'a\x80')
            self.assertEqual(
                u'\udc80'.encode(encoding, 'add_one_codepoint'),
                b'\x80')
            self.assertEqual(
                u'a\udc80b'.encode(encoding, 'add_one_codepoint'),
                b'a\x80b')

    def test_add_utf16_bytes(self):
        self.assertEqual(
            u'\udc80'.encode('utf-16', 'add_utf16_bytes'),
            b'ab')
        self.assertEqual(
            u'\udc80'.encode('utf-16-le', '
