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
    # test UTF-16
    # surrogate pairs
    assert codecs.utf_16_encode("\U00010000") == (b'\xd8\x00\xdc\x00', 2)
    assert codecs.utf_16_encode("\U00023456") == (b'\xd8\x23\x56', 2)
    assert codecs.utf_16_encode("\U00023456\U00010000") == (b'\xd8\x23\x56\xd8\x00\xdc\x00', 4)

    # non-BMP characters
    assert codecs.utf_16_encode("\U00012345") == (b'\xd8\x12\x34\xdd\x45', 4)
    assert codecs.utf_16_encode("\U00100000") == (b'\xdb\x10\x00', 2)
    assert codecs.utf_16_encode("\U0010fffd") == (b'\xdb\x10
