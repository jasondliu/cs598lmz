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

# unicode
for encoding in ["utf-8", "utf-16", "utf-16-le", "utf-16-be", "utf-32",
                 "utf-32-le", "utf-32-be"]:
    try:
        u"\u00a0".encode(encoding, "add_one_codepoint")
    except UnicodeEncodeError as e:
        print(e.object)
        print(e.start)
        print(e.end)
        print(e.reason)
    print()

# bytes
for encoding in ["utf-8", "utf-16", "utf-16-le", "utf-16-be", "utf-32",
                 "utf-32-le", "utf-32-be"]:
    try:
        b"\u00a0".decode(encoding, "add_one_codepoint")
    except UnicodeDecodeError as e:
        print(e.object)
        print(e.start)
        print(e.end)
        print(e.reason)
