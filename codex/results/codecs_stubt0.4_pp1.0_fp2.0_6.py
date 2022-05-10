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

#
#   Encode
#

def test_encode(encoding):
    # Test that the error handler is called
    u = chr(0x10FFFF)
    try:
        s = u.encode(encoding)
    except UnicodeEncodeError as exc:
        s = exc.object.encode(encoding, "add_one_codepoint")
    assert s == b"a"

    # Test that the error handler is called
    u = chr(0x10FFFF)
    try:
        s = u.encode(encoding)
    except UnicodeEncodeError as exc:
        s = exc.object.encode(encoding, "add_utf16_bytes")
    assert s == b"ab"

    # Test that the error handler is called
    u = chr(0x10FFFF)
    try:
        s = u.encode(encoding)
    except UnicodeEncodeError as exc:
        s = exc.object.encode(encoding, "add_utf32_bytes")
    assert s ==
