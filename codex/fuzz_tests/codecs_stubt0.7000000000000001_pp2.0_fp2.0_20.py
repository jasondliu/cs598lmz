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

def test_utf16_surrogates(encoding):
    test_string = "a\ud800\udc00b"
    codecs.encode(test_string, encoding)
    codecs.encode(test_string, encoding, errors="add_one_codepoint")
    codecs.encode(test_string, encoding, errors="add_utf16_bytes")
    codecs.encode(test_string, encoding, errors="add_utf32_bytes")

def test_utf32_surrogates(encoding):
    test_string = "a\ud800\udc00b"
    codecs.encode(test_string, encoding)
    codecs.encode(test_string, encoding, errors="add_one_codepoint")
    codecs.encode(test_string, encoding, errors="add_utf16_bytes")
    codecs.encode(test_string, encoding, errors="add_utf32_bytes")

test_utf16_surrogates("utf-16")
test_utf16_surrog
