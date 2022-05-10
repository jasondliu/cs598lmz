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

class EncodeDecodeTest(unittest.TestCase):
    def check_encode(self, encoding, input, output, decoded="h\xe9l\u0647o, le m\u0647\xf9nde"):
        self.assertEqual(input.encode(encoding), output)
        self.assertEqual(input.encode(encoding, "strict"), output)
        self.assertEqual(input.encode(encoding, "replace"), output)

    def check_encode_decode(self, encoding, input, output):
        self.check_encode(encoding, input, output)
        self.assertEqual(input, bytes(output).decode(encoding))

    def test_ascii_latin1(self):
        for encoding in ["ascii", "iso8859-1"]:
            self.check_encode_decode(encoding, "h\xe9l\u0647o, le m\u0647\xf9nde", b'h\xe9l\
