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

# Test UTF-8

assert u"\x80".encode("utf-8", "strict") == b"\xc2\x80"
assert u"\x80".encode("utf-8", "replace") == b"?\x80"
assert u"\x80".encode("utf-8", "ignore") == b""
assert u"\x80".encode("utf-8", "add_one_codepoint") == b"a\x80"
assert u"\x80".encode("utf-8", "add_utf16_bytes") == b"ab\x80"
assert u"\x80".encode("utf-8", "add_utf32_bytes") == b"abcd\x80"

assert b"\xc2\x80".decode("utf-8", "strict") == u"\x80"
assert b"\xc2\x80".decode("utf-8", "replace") == u"\ufffd\x80"
assert b"\xc2\x80".decode("utf-
