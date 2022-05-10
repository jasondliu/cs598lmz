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

def test_unicode_internal_encode_error():
    class IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input, final=False):
            return codecs.charmap_encode(input, self.errors, encoding_table)[0]

        def reset(self):
            codecs.IncrementalEncoder.reset(self)

        def getstate(self):
            return codecs.IncrementalEncoder.getstate(self)[0]

        def setstate(self, state):
            codecs.IncrementalEncoder.setstate(self, (state, 0))

    class IncrementalDecoder(codecs.IncrementalDecoder):
        def decode(self, input, final=False):
            return codecs.charmap_decode(input, self.errors, decoding_table)[0]

        def reset(self):
            codecs.IncrementalDecoder.reset(self)

        def getstate(self):
            return codecs.IncrementalDecoder.getstate(self)[0]

        def setstate(
