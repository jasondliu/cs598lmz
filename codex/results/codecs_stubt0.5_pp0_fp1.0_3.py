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

def check_decode_unicode(encoding, errors):
    decoder = codecs.getdecoder(encoding)
    decoder.errors = errors
    result, length = decoder(b'\xfe\xff\x00\x00')
    assert result == 'a\udc80'
    assert length == 4

def check_decode_bytes(encoding, errors):
    decoder = codecs.getdecoder(encoding)
    decoder.errors = errors
    result, length = decoder(b'\xfe\xff\x00\x00')
    assert result == b'ab'
    assert length == 4

def check_encode_unicode(encoding, errors):
    encoder = codecs.getencoder(encoding)
    encoder.errors = errors
    result, length = encoder('\udc80')
    assert result == b'\x00\x00'
    assert length == 1

def check_encode_bytes(encoding, errors):
    encoder = codecs.getencoder
