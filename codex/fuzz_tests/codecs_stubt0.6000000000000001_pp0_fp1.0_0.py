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
    # test utf-7
    assert "abc".encode("utf-7") == b"+AIM,BAA-", "utf-7"
    assert "+AIM,BAA-".decode("utf-7") == "abc", "utf-7"

    # test utf-8
    assert "abc".encode("utf-8") == b"abc", "utf-8"
    assert b"abc".decode("utf-8") == "abc", "utf-8"

    # test utf-8 with surrogate pairs
    assert "\U00023456".encode("utf-8") == b"\xf0\xa2\x91\x96", "utf-8"
    assert b"\xf0\xa2\x91\x96".decode("utf-8") == "\U00023456", "utf-8"

    # test utf-8 with lone surrogates
    assert "\ud800".encode("utf-8", "replace") == b"?", "utf-8"
    assert "\udc00
