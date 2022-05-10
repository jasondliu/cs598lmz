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

def test_decode_error():
    # decoder-specific errors
    codecs.decode("abc", "ascii", "replace")
    codecs.decode("abc", "ascii", "ignore")
    codecs.decode("abc", "ascii", "xmlcharrefreplace")
    codecs.decode("abc", "ascii", "backslashreplace")
    codecs.decode("abc", "ascii", "namereplace")
    codecs.decode("abc", "ascii", "add_one_codepoint")
    codecs.decode("abc", "ascii", "add_utf16_bytes")
    codecs.decode("abc", "ascii", "add_utf32_bytes")
    codecs.decode("abc", "ascii", "strict")
    codecs.decode("abc", "ascii", "surrogateescape")
    codecs.decode("abc", "ascii", "surrogatepass")
    codecs.decode("abc
