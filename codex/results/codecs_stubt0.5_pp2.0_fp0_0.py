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

def test_utf16_decode_error(self):
    self.assertEqual(b'\xff\xfe\x00\x00'.decode('utf-16', 'add_one_codepoint'),
                     'a\x00')
    self.assertEqual(b'\xff\xfe\x00\x00'.decode('utf-16', 'add_utf16_bytes'),
                     'ab\x00')
    self.assertRaises(UnicodeDecodeError, b'\xff\xfe\x00\x00'.decode,
                      'utf-16', 'add_utf32_bytes')

def test_utf16_le_decode_error(self):
    self.assertEqual(b'\x00\x00\x00'.decode('utf-16-le', 'add_one_codepoint'),
                     'a\x00\x00')
    self.assertEqual(b'\x00\x00\x00'.decode('utf-16-le', 'add_utf16_bytes
