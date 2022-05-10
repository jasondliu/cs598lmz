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

def test_encode(encoding):
    u = '\u3042\u3044\u3046'
    codec = codecs.getencoder(encoding)
    result, bytes = codec(u, "add_one_codepoint")
    assert result == u + 'a'
    assert bytes == 3

def test_decode(encoding):
    b = b'\x82\xa0\x82\xa2\x82\xa4'
    codec = codecs.getdecoder(encoding)
    result, bytes = codec(b, "add_utf16_bytes")
    assert result == '\u3042\u3044\u3046ab'
    assert bytes == 6

def test_utf32_decode(encoding):
    b = b'\x00\x00\x30\x42\x00\x00\x30\x44\x00\x00\x30\x46'
    codec = codecs.getdecoder(encoding)
    result, bytes = codec(b, "add
