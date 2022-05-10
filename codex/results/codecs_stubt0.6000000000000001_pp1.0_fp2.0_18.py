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

# UCS2
exc_handler = codecs.lookup_error("add_one_codepoint")
assert exc_handler(b"a", "ascii", 1, 2, "test") == ("a", 1)
assert exc_handler(b"a", "utf-16", 1, 2, "test") == ("a", 1)
assert exc_handler(b"a", "utf-32", 1, 2, "test") == ("a", 1)

exc_handler = codecs.lookup_error("add_utf16_bytes")
assert exc_handler(b"a", "ascii", 1, 2, "test") == (b'ab', 1)
assert exc_handler(b"a", "utf-16", 1, 2, "test") == (b'ab', 1)
assert exc_handler(b"a", "utf-32", 1, 2, "test") == (b'ab', 1)

# UCS4
exc_handler = codecs.lookup_error("add_one_codepoint")
assert exc_handler(b"
