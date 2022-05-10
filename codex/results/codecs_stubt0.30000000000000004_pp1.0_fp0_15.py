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
    # Test UTF-16
    for encoding in ("utf-16", "utf-16-le", "utf-16-be"):
        # Test that the surrogate pair is decoded correctly
        assert codecs.decode(b'\x00\xd8\x00\xdc', encoding) == '\U00010348'
        # Test that the surrogate pair is encoded correctly
        assert codecs.encode('\U00010348', encoding) == b'\x00\xd8\x00\xdc'
        # Test that the surrogate pair is decoded correctly with errors
        assert codecs.decode(b'\x00\xd8\x00\xdc\x00\xdc', encoding, "add_one_codepoint") == '\U00010348\U00010348'
        # Test that the surrogate pair is encoded correctly with errors
        assert codecs.encode('\U00010348\U00010348', encoding, "add_utf16_bytes") == b'\x00\xd8\x00\xdc
