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

def test_decoding_error_handling(source, errors, decoder):
    encoded, decoded = source
    d = codecs.getincrementaldecoder(decoder)(errors)
    for s in encoded:
        r = d.decode(s)
    assert d.decode(b"", True) == decoded

def test_encoding_error_handling(source, errors, decoder):
    encoded, decoded = source
    d = codecs.getencoder(decoder)(errors)
    for s in decoded:
        r = d.encode(s)
    r = d.encode("", True)
    assert source == r

def test_decoding_error_no_raise():
    try:
        codecs.decode("a", "unknown", errors="a", final=True)
    except LookupError:
        py.test.skip("decoding error is unknown")

def test_encoding_error_no_raise():
    try:
        codecs.encode("a", "unknown", errors="
