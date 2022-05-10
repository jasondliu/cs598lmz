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

def test_main():
    # Test UTF-8
    assert u"\u3042".encode("utf-8", "add_one_codepoint") == b"a\xe3\x81\x82"
    assert u"\u3042".encode("utf-8", "add_utf16_bytes") == b"ab\xe3\x81\x82"
    assert u"\u3042".encode("utf-8", "add_utf32_bytes") == b"abcd\xe3\x81\x82"

    # Test UTF-16
    assert u"\u3042".encode("utf-16", "add_one_codepoint") == b"a\xff\xfe\x42\x30"
    assert u"\u3042".encode("utf-16", "add_utf16_bytes") == b"ab\xff\xfe\x42\x30"
    assert u"\u3042".encode("utf-16", "add_utf32_bytes") == b"abcd\xff
