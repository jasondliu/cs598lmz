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
    def test_make_encoder_with_invalid_errors_value(self):
        with self.assertRaises(TypeError):
            codecs.Encoder('utf-8', errors=123)

    def test_make_decoder_with_invalid_errors_value(self):
        with self.assertRaises(TypeError):
            codecs.Decoder('utf-8', errors=123)

    def test_encode_with_invalid_errors_value(self):
        with self.assertRaises(TypeError):
            ''.encode('utf-8', errors=123)

    def test_decode_with_invalid_errors_value(self):
        with self.assertRaises(TypeError):
            b''.decode('utf-8', errors=123)

    def test_register_error(self):
        with self.assertRaises(TypeError):
            codecs.register_error('err', 123)
        with self.assertRaises(ValueError):
           
