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

# UTF-16
for encoding in ["utf-16", "utf-16-be", "utf-16-le"]:
    # Test decoding with a single surrogate
    for surrogate in [b"\xD8\x00", b"\xDC\x00"]:
        try:
            surrogate.decode(encoding)
        except UnicodeDecodeError as exc:
            # Check that the replacement character was inserted at the right
            # position
            assert exc.start == 0
            assert exc.end == 2
            assert exc.object == surrogate
            assert exc.reason == "invalid start byte"
            assert exc.encoding == encoding
            assert exc.args == (
                surrogate, 0, 2, "invalid start byte")
            assert exc.__cause__ is None

    # Test decoding with a high surrogate followed by an invalid character
    for invalid in [b"\x00", b"\xD8\x00", b"\xDC\x00"]:
        try:
            (b"\xD8\x00" + invalid).decode(encoding
