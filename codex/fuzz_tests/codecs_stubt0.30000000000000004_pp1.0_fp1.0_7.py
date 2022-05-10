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

# Test that we can decode with an error handler that adds a single
# codepoint, and that the error handler is called with the correct
# start position.

def test_decode_error_handler_add_one_codepoint():
    # Test with a single-byte codec
    s = b'\xff'
    for errors in ["strict", "ignore", "replace", "add_one_codepoint"]:
        assert codecs.decode(s, "latin-1", errors=errors) == '\ufffd'
    for errors in ["strict", "ignore", "replace"]:
        assert codecs.decode(s, "ascii", errors=errors) == '\ufffd'
    for errors in ["strict", "ignore", "replace", "add_one_codepoint"]:
        assert codecs.decode(s, "utf-8", errors=errors) == '\ufffd'
    for errors in ["strict", "ignore", "replace", "add_one_codepoint"]:
        assert codecs.decode(
