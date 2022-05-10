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

# test decoding
for enc in ("utf-8", "utf-16-le"):
    for errors in (None, "add_one_codepoint", "add_utf16_bytes"):
        print(enc, errors)
        # utf8 <-> unicode
        u = b'\xff'.decode(enc, errors)
        print(type(u), repr(u))
        b = u.encode(enc, errors)
        print(type(b), repr(b))

# test roundtrip
for enc in ("utf-8", "utf-16-le", "utf-32-le"):
    for errors in (None, "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
        print(enc, errors)
        u = u'\u1234'
        b = u.encode(enc, errors)
        if b[0] == 0xff:
            u = b'\xff'.decode(enc, errors)
        else:
            u = b.decode(
