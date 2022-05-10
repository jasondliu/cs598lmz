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

class TestUnicodeDecodeError(unittest.TestCase):

    def test_add_one_codepoint(self):
        # Test that adding one codepoint works
        s = b'ab\xff'
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            with self.subTest(encoding=encoding):
                self.assertEqual(s.decode(encoding, 'add_one_codepoint'), 'ab\ufffd')

    def test_add_utf16_bytes(self):
        # Test that adding two UTF-16 bytes works
        s = b'ab\xff'
        for encoding in ('utf-16', 'utf-32'):
            with self.subTest(encoding=encoding):
                self.assertEqual(s.decode(encoding, 'add_utf16_bytes'), 'ab\ufffd')

    def test_add_utf32_bytes(self):
        # Test that adding four UTF-32 bytes works
        s = b'ab\xff'
        for
