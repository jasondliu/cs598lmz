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

def test_bom_decoding_errors(bom, error_handler):
    """Decoding errors with a BOM."""

    # Decoding a stream of bytes starting with a BOM should
    # never raise a decoding error. The BOM should be understood as a
    # zero-width character and have no effect on the decoding.
    # Only the bytes after the BOM should be decoded.

    # Partial BOM
    assert bom[:1].decode("utf-8", errors=error_handler) == "a"

    # Partial BOM
    assert bom[:2].decode("utf-8", errors=error_handler) == "a"

    # Invalid continuation byte
    assert (b"\x80" + bom[2:]).decode("utf-8", errors=error_handler) == "a"

    # Unexpected BOM in the middle of the stream
    assert ("\uff76" + bom[1:]).decode("utf-8", errors=error_handler) == "a"

    # Two BOMs in a row (should be correctly encoded)
