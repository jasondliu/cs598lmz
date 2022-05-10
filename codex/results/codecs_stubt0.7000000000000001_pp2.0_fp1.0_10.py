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

b = b"abcd"

for enc, expected in [("utf-8", b"abcd"),
                      ("utf-16", b"\xff\xfea\0b\0"),
                      ("utf-32", b"\xff\xfe\0\0a\0\0\0b\0\0\0")]:
    print(enc)
    print(b.decode(enc))
    print(b.decode(enc, "add_one_codepoint"))
    print(b.decode(enc, "add_utf16_bytes"))
    print(b.decode(enc, "add_utf32_bytes"))

print("utf-16-le")
print(b"\xff\xfea\0b\0".decode("utf-16-le"))
print(b"\xfe\xffa\0b\0".decode("utf-16-le"))
print(b"\xff\xffa\0b\0".decode("utf-16-le"))
print(b"\xfe\xffa
