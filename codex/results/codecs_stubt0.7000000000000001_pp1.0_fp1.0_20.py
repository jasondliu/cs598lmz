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

def test_utf16_decode_error(codec):
    # test UTF-16-BE and UTF-16-LE
    # UTF-16-LE with BOM
    assert codec.decode(b'ab\xff\xfe\x00\x00', "replace", "add_one_codepoint") == "ab\u0000"
    assert codec.decode(b'ab\xff\xfe\x00\x00', "replace", "add_utf16_bytes") == "ab\u00ab"
    assert codec.decode(b'ab\xff\xfe\x00\x00', "replace", "add_utf32_bytes") == "ab\U0000abcd"
    # UTF-16-LE without BOM
    assert codec.decode(b'ab\x00\x00', "replace", "add_one_codepoint") == "ab\u0000"
    assert codec.decode(b'ab\x00\x00', "replace", "add_utf16_bytes") == "ab\u00ab"

