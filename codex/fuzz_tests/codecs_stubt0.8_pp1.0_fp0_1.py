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

def test_error_callbacks():
    # test error callbacks with decoding
    assert "ab" == "a\x80".decode("ascii", "add_one_codepoint")
    assert "ab" == "a\x80".decode("utf-8", "add_one_codepoint")
    assert "ab" == "a\x80".decode("latin-1", "add_one_codepoint")

    # test error callbacks with encoding
    assert "ab" == "abc".encode("ascii", "add_one_codepoint")
    assert "ab" == "abc".encode("utf-8", "add_one_codepoint")
    assert "ab" == "abc".encode("latin-1", "add_one_codepoint")

    # test error callbacks with decoding
    assert "ab" == b'\x00\x80'.decode("ascii", "add_utf16_bytes")
    assert "ab" == b'\x00\x80'.decode("utf
