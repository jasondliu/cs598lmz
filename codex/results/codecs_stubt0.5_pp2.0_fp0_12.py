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

# Test UTF-8
def test_utf8(encoding):
    uc = b"\xd4\x80\x00\xd4\x80\x00"
    uc = uc.decode(encoding)
    assert uc == "\U00010000"

    uc = b"\xd4\x80\x00\xd4\x80\x00\xd4\x80\x00"
    uc = uc.decode(encoding, "add_one_codepoint")
    assert uc == "\U00010000a"

    uc = b"\xed\xa0\x80\xed\xb0\x80"
    uc = uc.decode(encoding)
    assert uc == "\U00010000"

    uc = b"\xed\xa0\x80\xed\xb0\x80\xed\xa0\x80"
    uc = uc.decode(encoding, "add_one_codepoint")
    assert uc == "\U
