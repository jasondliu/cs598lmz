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

# FIXME: test that the codecs error handler works properly

def test(s, enc, decoder_error_handler):
    decoded = codecs.decode(s, enc, decoder_error_handler)
    encoded = codecs.encode(decoded, enc)
    assert(encoded == s)

def test2(s, enc, decoder_error_handler):
    decoded = codecs.decode(s, enc, decoder_error_handler)
    encoded = codecs.encode(decoded, enc)
    assert(encoded == s)

def test_one_codepoint(enc):
    test("\xc2\x00", enc, "add_one_codepoint")

def test_utf16_bytes(enc):
    test("\x00\x00", enc, "add_utf16_bytes")

def test_utf32_bytes(enc):
    test("\x00\x00\x00\x00", enc, "add_utf32_bytes")

def test_one_cod
