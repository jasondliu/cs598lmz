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

def test_unicode_decode(encoding, errors, pattern, bytes=b"\xed\xa0\x80"):
    decoded = pattern.decode(encoding, errors)
    assert len(decoded) == len(bytes)
    assert len(decoded) == pattern.size

def test_unicode_encode(pattern, encoding, errors, string="a"):
    encoded = string.encode(encoding, errors)
    assert len(encoded) == len(pattern)
    assert encoded.find(pattern) >= 0
    assert encoded.endswith(pattern)

def test_bytes_decode(pattern, encoding, errors, string="a"):
    encoded = string.encode(encoding, "strict")
    assert len(encoded) == len(pattern)
    assert encoded.find(pattern) >= 0
    decoded, bytes = pattern.decode(encoding, errors)
    assert len(decoded) == len(string)
    assert len(bytes) == len(pattern)
    assert bytes.find(pattern
