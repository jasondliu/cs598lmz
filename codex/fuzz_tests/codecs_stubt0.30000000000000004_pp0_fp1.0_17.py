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

# Test that the surrogatepass error handler works correctly

def test_surrogatepass():
    # UTF-16
    assert codecs.utf_16_decode(b'\x00\xd8\x00\xdc', "surrogatepass") == (
        u'\U00010348', 4)
    assert codecs.utf_16_decode(b'\x00\xd8\x00\xdc\x00\x00', "surrogatepass") == (
        u'\U00010348', 4)
    assert codecs.utf_16_decode(b'\x00\xd8\x00\xdc\x00\x00', "surrogatepass",
                                final=True) == (u'\U00010348', 4)
    assert codecs.utf_16_decode(b'\x00\xd8\x00\xdc\x00\x00', "surrogatepass",
                                final=False) == (u'\U00010348', 6)
    assert codecs.utf
