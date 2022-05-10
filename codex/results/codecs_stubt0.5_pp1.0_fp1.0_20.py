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

class UnicodeErrorTest(unittest.TestCase):

    def test_decode(self):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            with self.subTest(encoding=encoding):
                self.assertEqual(u'\ufffd',
                                 u'\x80'.encode(encoding, 'replace').decode(encoding))
                self.assertEqual(u'\ufffd',
                                 u'\xff'.encode(encoding, 'replace').decode(encoding))
                self.assertEqual(u'\ufffd\ufffd',
                                 u'\x80\xff'.encode(encoding, 'replace').decode(encoding))
                self.assertEqual(u'\ufffd',
                                 u'\xff'.encode(encoding, 'replace').decode(encoding))
                self.assertEqual(u'\ufffd\ufffd',
                                 u'\x80\xff'.encode(encoding, 'replace').decode(enc
