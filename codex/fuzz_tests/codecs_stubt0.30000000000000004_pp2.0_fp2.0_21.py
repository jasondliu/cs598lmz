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

# test unicode-internal
for encoding in ["utf-7", "utf-8", "utf-16", "utf-32"]:
    print(encoding)
    s = "abc"
    u = s.encode(encoding, "add_one_codepoint")
    print(u)
    print(u.decode(encoding))
    print(u.decode(encoding, "ignore"))
    print(u.decode(encoding, "replace"))
    print(u.decode(encoding, "add_one_codepoint"))
    print(u.decode(encoding, "add_utf16_bytes"))
    print(u.decode(encoding, "add_utf32_bytes"))
    print()

# test unicode-external
for encoding in ["ascii", "latin-1", "iso8859-1", "iso8859-15"]:
    print(encoding)
    s = "abc"
    u = s.encode(encoding, "add_one_codepoint")

