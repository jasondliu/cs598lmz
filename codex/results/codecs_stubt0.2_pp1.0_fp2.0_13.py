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
    def test_decode_utf8(self):
        self.assertEqual(codecs.decode(b'\x80', 'utf-8', 'strict'), '\uFFFD')
        self.assertEqual(codecs.decode(b'\x80', 'utf-8', 'replace'), '\uFFFD')
        self.assertEqual(codecs.decode(b'\x80', 'utf-8', 'ignore'), '')
        self.assertEqual(codecs.decode(b'\x80', 'utf-8', 'add_one_codepoint'), 'a\uFFFD')
        self.assertEqual(codecs.decode(b'\x80', 'utf-8', 'add_utf16_bytes'), 'a\uFFFD')
        self.assertEqual(codecs.decode(b'\x80', 'utf-8', 'add_utf32_bytes'), 'a\uFFFD')

   
