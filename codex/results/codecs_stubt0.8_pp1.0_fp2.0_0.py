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

### Encoding

class EncodingTest:

    encoding = None

    def test_simpleencode(self):
        assert self.s.encode(self.encoding) == self.encoded

    def test_simpleencode_errors(self):
        assert self.s.encode(self.encoding, "ignore") == self.encoded
        assert self.s.encode(self.encoding, "replace") == self.encoded_replace
        #assert self.s.encode(self.encoding, "add_one_codepoint") == self.encoded_add_one_codepoint
        #assert self.s.encode(self.encoding, "add_utf16_bytes") == self.encoded_add_utf16_bytes
        #assert self.s.encode(self.encoding, "add_utf32_bytes") == self.encoded_add_utf32_bytes

    def test_encode_errors(self):
        assert self.s.encode(self.encoding, "ignore") == self.encoded

