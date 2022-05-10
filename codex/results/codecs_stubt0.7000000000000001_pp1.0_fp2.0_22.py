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

def create_test_function(encoding, decoding_error_handler, encoding_error_handler):
    def test_function(self):
        if encoding_error_handler is not None:
            self.assertRaises(UnicodeEncodeError, encoding.encode,
                              '\u0C80', encoding_error_handler)
        if decoding_error_handler is not None:
            self.assertRaises(UnicodeDecodeError, encoding.decode,
                              b'\xC0', decoding_error_handler)
    return test_function

class TestErrorHandling(unittest.TestCase):
    def test_error_handling_codec(self):
        self.assertRaises(UnicodeEncodeError, '\u0C80'.encode, 'ascii')
        self.assertRaises(UnicodeDecodeError, b'\xC0'.decode, 'ascii')
        self.assertRaises(UnicodeEncodeError, '\u0C80'.encode, 'ascii',
