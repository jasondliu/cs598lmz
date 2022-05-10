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

# 2-byte char
print("\u1234".encode("utf-16", "add_one_codepoint"))
print("\u1234".encode("utf-16", "add_utf16_bytes"))

# 4-byte char
print("\U00012345".encode("utf-32", "add_one_codepoint"))
print("\U00012345".encode("utf-32", "add_utf32_bytes"))

# surrogate pairs
print("\uD834\u1234".encode("utf-16", "add_one_codepoint"))
print("\uD834\u1234".encode("utf-16", "add_utf16_bytes"))
print("\uD834\u1234".encode("utf-32", "add_one_codepoint"))
print("\uD834\u1234".encode("utf-32", "add_utf32_bytes"))

# null char
print("\0".encode("utf-16", "add_one_codepoint
