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

def test_decode_error_handling():
    # Test that the correct exception is raised when a decode error occurs
    # and the error handling is "strict"
    for encoding in ("utf-8", "utf-16", "utf-32"):
        # Check that the correct exception is raised
        for error_handler in ("strict", "ignore", "replace"):
            try:
                codecs.decode(b"\xff", encoding, error_handler)
            except UnicodeDecodeError as exc:
                assert exc.encoding == encoding
                assert exc.object == b"\xff"
                assert exc.start == 0
                assert exc.end == 1
                assert exc.reason == "invalid start byte"
            else:
                assert error_handler == "ignore"

        # Check that the correct exception is raised
        for error_handler in ("strict", "ignore", "replace"):
            try:
                codecs.decode(b"\xff\x00", encoding, error_handler)
            except UnicodeDecodeError as exc:
                assert exc.
