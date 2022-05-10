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

# Test decoding

def test_decode_latin1(self):
    self.assertEqual(b'abc'.decode('latin-1'), 'abc')
    self.assertEqual(b'\xe9'.decode('latin-1'), '\xe9')
    self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'latin-1')
    self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'latin-1', 'strict')
    self.assertEqual(b'\xff'.decode('latin-1', 'ignore'), '')
    self.assertEqual(b'\xff'.decode('latin-1', 'replace'), '\ufffd')
    self.assertEqual(b'\xff'.decode('latin-1', 'add_one_codepoint'), '\ufffd')
    self.assertEqual(b'\xff\xff'.decode('latin-1', 'add_one_codepoint'), '\
