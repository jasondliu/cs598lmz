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
    # Error handling works
    # Error handling works when used in incremental decoder
    # Error handling works when used in incremental encoder

    # UnicodeDecodeError
    assert codecs.charmap_decode(b"\x00\x01\x02", "strict", {0:None,1:"a"}) == ("a", 3)
    assert codecs.charmap_decode(b"\x00\x01\x02", "replace", {0:None,1:"a"}) == ("a\ufffd", 3)
    assert codecs.charmap_decode(b"\x00\x01\x02", "ignore", {0:None,1:"a"}) == ("a", 2)
    assert codecs.charmap_decode(b"\x00\x01\x02", "add_one_codepoint", {0:None,1:"a"}) == ("aa", 3)
    assert codecs.charmap_decode(b"\x00\x01\x00\
