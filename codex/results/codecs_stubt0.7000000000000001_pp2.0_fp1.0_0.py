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

# Test UTF-8 and UTF-16.
def test_utf8_utf16_decoding_error(encoding):
    # Test decoding errors with surrogateescape
    assert b'\xff'.decode(encoding, 'surrogateescape') == '\udcff'
    assert b'\xed\x9f\xbf'.decode(encoding, 'surrogateescape') == '\udfff'
    assert b'\xed\xa0\x80'.decode(encoding, 'surrogateescape') == '\ud800'
    assert b'\xed\xbf\xbf'.decode(encoding, 'surrogateescape') == '\udbff'
    assert b'\xed\x80\x80'.decode(encoding, 'surrogateescape') == '\udc00'
    assert b'\xed\x8f\xbf'.decode(encoding, 'surrogateescape') == '\udcff'
    assert b'\xed\x80\x80\xed\x
