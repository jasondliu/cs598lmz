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

def test_unicode_append(self):
    # Appending to a unicode string
    self.assertEqualError(UnicodeTest.test_unicode_append,
                          UnicodeDecodeError,
                          'utf-8', b'\xf1\x80\x80', 0, 1,
                          'add_one_codepoint',
                          "append a UnicodeDecodeError to a unicode string")
    # Appending to a bytearray
    self.assertEqualError(UnicodeTest.test_unicode_append,
                          UnicodeDecodeError,
                          'utf-16', b'\x00\xf1\x80\x80', 0, 4,
                          'add_utf16_bytes',
                          "append a UnicodeDecodeError to a bytearray")
    # Appending to a bytearray
    self.assertEqualError(UnicodeTest.test_unicode_append,
                          UnicodeDecodeError,
                          'utf-32', b'\x00\x00\
