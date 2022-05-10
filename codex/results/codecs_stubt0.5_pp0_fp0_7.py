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

    def check_decode(self, encoding, input, output, errors=None):
        if errors is None:
            errors = "strict"
        self.assertEqual(codecs.decode(input, encoding, errors), output)
        self.assertEqual(input.decode(encoding, errors), output)

    def check_encode(self, encoding, input, output, errors=None):
        if errors is None:
            errors = "strict"
        self.assertEqual(codecs.encode(input, encoding, errors), output)
        self.assertEqual(input.encode(encoding, errors), output)

    def test_latin_1(self):
        self.check_encode("latin-1", "abc\xe9\u20ac", b"abc\xe9\xe2\x82\xac")
        self.check_encode("latin-1", "abc\xe9\u20ac", b"abc\xe9\xe
