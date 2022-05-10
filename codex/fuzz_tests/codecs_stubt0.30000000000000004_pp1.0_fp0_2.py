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

# Test that the encoder/decoder can handle a buffer
# that is not aligned to the code unit size.

def test_buffer_not_aligned(encoding, errors):
    decoder = codecs.getincrementaldecoder(encoding)(errors)
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.decode(b'\xff\xff\xff')
    decoder.
