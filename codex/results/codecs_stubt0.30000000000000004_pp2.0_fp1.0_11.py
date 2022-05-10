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

# utf-16

def test_utf16_decode(encoding):
    s = b'\xff\xfex\x00\x00'
    assert codecs.decode(s, encoding, "add_one_codepoint") == "aex"
    assert codecs.decode(s, encoding, "add_utf16_bytes") == "abex"
    assert codecs.decode(s, encoding, "add_utf32_bytes") == "abcdex"

def test_utf16_encode(encoding):
    s = '\udc80x'
    assert codecs.encode(s, encoding, "add_one_codepoint") == b'\xff\xfex'
    assert codecs.encode(s, encoding, "add_utf16_bytes") == b'\xff\xfex\x00\x00'
    assert codecs.encode(s, encoding, "add_utf32_bytes") == b'\xff\xfex\x00\x00\x00\x00'


