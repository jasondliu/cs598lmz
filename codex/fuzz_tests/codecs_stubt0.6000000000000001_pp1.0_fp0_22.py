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

def encode(exc):
    return ("a", exc.start)

def decode(exc):
    return ("a", exc.start)

codecs.register_error("encode", encode)
codecs.register_error("decode", decode)

def test_main():
    import sys

    if sys.platform == "win32":
        # check that the surrogateescape error handler doesn't eat the
        # exception, since it doesn't touch the byte stream
        with pytest.raises(UnicodeDecodeError):
            "ab\xff".encode("utf-16-le", "surrogateescape")

    # check that the surrogateescape error handler doesn't eat the
    # exception, since it doesn't touch the byte stream
    with pytest.raises(UnicodeDecodeError):
        b"ab\xff".decode("utf-16-le", "surrogateescape")

    # check that the surrogateescape error handler doesn't eat the
    # exception, since it doesn't touch the byte stream
    with pytest.raises(Unicode
