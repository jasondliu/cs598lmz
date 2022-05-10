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

print(u"a".encode("ascii", "add_one_codepoint"))
print(str(u"a".encode("utf16", "add_utf16_bytes"), "utf16"))
print(str(u"a".encode("utf32", "add_utf32_bytes"), "utf32"))
