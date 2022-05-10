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

for encoding, test_string in [
        ('utf-16', b"a\x00b\x00"),
        ('utf-32', b"a\x00\x00\x00b\x00\x00\x00"),
        ]:
    # unicode -> bytes
    assert test_string.decode(encoding, 'add_one_codepoint') == \
        "a\ua000b\ua000"
    # bytes -> unicode
    assert test_string.decode(encoding, 'add_utf16_bytes') == \
        "a\x00b\x00\x00b\x00"
    assert test_string.decode(encoding, 'add_utf32_bytes') == \
        "a\x00\x00\x00b\x00\x00\x00\x00\x00\x00b\x00\x00\x00"

def raise_exception(encoding, exc):
    if isinstance(exc, UnicodeDecodeError):
        s, start, end, reason
