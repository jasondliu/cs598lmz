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

def test_utf16_be_decode_error(self):
    # utf-16-be codec, decoding
    self.assertRaises(UnicodeDecodeError, '\xff\xfea'.decode, 'utf-16-be')
    self.assertRaises(UnicodeDecodeError, '\xff\xfeab'.decode, 'utf-16-be')
    self.assertRaises(UnicodeDecodeError, '\xff\xfeabc'.decode, 'utf-16-be')
    self.assertRaises(UnicodeDecodeError, '\xff\xfeabcd'.decode, 'utf-16-be')
    self.assertRaises(UnicodeDecodeError, '\xff\xfeabcde'.decode, 'utf-16-be')
    self.assertRaises(UnicodeDecodeError, '\xff\xfeabcdef'.decode, 'utf-16-be')
    self.assertRaises(UnicodeDecodeError, '\xff\xfeabcdefg'.
