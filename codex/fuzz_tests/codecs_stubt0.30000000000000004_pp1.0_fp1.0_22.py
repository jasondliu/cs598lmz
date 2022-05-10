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

def encode_utf8(s):
    return s.encode("utf-8")

def encode_utf16(s):
    return s.encode("utf-16")

def encode_utf32(s):
    return s.encode("utf-32")

def decode_utf8(s):
    return s.decode("utf-8", "add_one_codepoint")

def decode_utf16(s):
    return s.decode("utf-16", "add_utf16_bytes")

def decode_utf32(s):
    return s.decode("utf-32", "add_utf32_bytes")

def test_encode_utf8():
    assert encode_utf8("\u1234") == b"\xe1\x88\xb4"
    assert encode_utf8("\ud800\udc00") == b"\xf0\x90\x80\x80"
    assert encode_utf8("\udbff\udfff") == b"\xef\xbf\xbf\
