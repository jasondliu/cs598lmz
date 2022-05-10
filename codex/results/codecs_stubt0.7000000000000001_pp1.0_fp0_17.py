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

def test_decode_errors():
    codecs.decode("abc", "ascii", "add_one_codepoint")
    codecs.decode(b"ab", "ascii", "add_utf16_bytes")
    codecs.decode(b"abcd", "ascii", "add_utf32_bytes")


def test_encode_errors():
    codecs.encode("abc", "ascii", "add_one_codepoint")
    codecs.encode(b"ab", "ascii", "add_utf16_bytes")
    codecs.encode(b"abcd", "ascii", "add_utf32_bytes")
