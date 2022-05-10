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

class TestCodecs(unittest.TestCase):

    def test_decode_error_handling(self):
        for encoding in 'utf-8', 'utf-16', 'utf-32':
            # Test errors in the middle of a string
            for i in range(1, len(b'\x80\x80\x80')):
                self.assertRaises(UnicodeDecodeError,
                                  codecs.decode, b'\x80\x80\x80', encoding)

            # Test errors at the beginning of a string
            self.assertRaises(UnicodeDecodeError,
                              codecs.decode, b'\x80\x80\x80', encoding)

            # Test errors at the end of a string
            self.assertRaises(UnicodeDecodeError,
                              codecs.decode, b'\x80\x80\x80', encoding)

    def test_decode_error_handling_with_replace(self):
        for encoding in 'utf-8', 'utf-16',
