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

# test codecs.encode()

# unicode -> str
assert codecs.encode("abc", "ascii") == b"abc"
assert codecs.encode("abc", "latin-1") == b"abc"
assert codecs.encode("abc", "utf-8") == b"abc"
assert codecs.encode("abc", "utf-16") == b"\xff\xfea\x00b\x00c\x00"
assert codecs.encode("abc", "utf-16-le") == b"a\x00b\x00c\x00"
assert codecs.encode("abc", "utf-16-be") == b"\x00a\x00b\x00c"
assert codecs.encode("abc", "utf-32") == b"\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00"
assert codecs.encode("abc", "utf-32-
