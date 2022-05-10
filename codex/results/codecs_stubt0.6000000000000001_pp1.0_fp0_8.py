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

def test_error_callback(encoding):
    # Test error callback
    #
    #     - try to encode a character not present in the encoding
    #     - try to decode an incomplete byte sequence
    #     - try to decode a sequence of bytes which is not a valid
    #       character in the encoding

    # test encoding

    # single character
    codecs.encode("a", encoding=encoding, errors="add_one_codepoint")

    # multiple characters
    codecs.encode("a\u1234\u5678", encoding=encoding, errors="add_one_codepoint")

    # test decoding

    # an incomplete byte sequence
    if encoding in ["utf-16", "utf-16-le", "utf-16-be"]:
        codecs.decode(b"a", encoding=encoding, errors="add_utf16_bytes")
    elif encoding in ["utf-32", "utf-32-le", "utf-32-be"]:
        codecs.decode(b"a", encoding=encoding, errors="add
