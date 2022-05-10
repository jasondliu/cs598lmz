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

b = bytes("\x80\x81\x82", "utf-8")
for name in list("utf_8", "utf-8"):

    s = b.decode(name)
    print(s, len(s))
    s = b.decode(name, "ignore")
    print(s, len(s))
    s = b.decode(name, "replace")
    print(s, len(s))
    s = b.decode(name, "add_one_codepoint")
    print(s, len(s))
    s = b.decode(name, "add_utf16_bytes")
    print(s, len(s))
    s = b.decode(name, "add_utf32_bytes")
    print(s, len(s))
    print()

b = bytes("\xff\xff\xff", "utf-16")
for name in list("utf_16", "utf-16"):

    s = b.decode(name)
    print(s, len(s))
   
