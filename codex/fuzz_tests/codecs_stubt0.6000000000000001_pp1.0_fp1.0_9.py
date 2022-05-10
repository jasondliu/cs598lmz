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

# The following tests test the behaviour of the codecs module and of the
# encodings package when errors occur.

class TestErrorHandling(unittest.TestCase):
    # Issue #7768: a UTF-16 encoded string with a lone surrogate should
    # raise a UnicodeDecodeError.
    def test_utf16_lone_surrogate(self):
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_le_decode,
                          b'\x00\xd8\x00', 'replace')
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_le_decode,
                          b'\x00\xdc\x00', 'replace')
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_be_decode,
                          b'\xd8\x00\x00', 'replace')
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_be_decode,
                          b'
