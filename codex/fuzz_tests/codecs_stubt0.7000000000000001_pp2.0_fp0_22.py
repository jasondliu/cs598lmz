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

for encoding in ["utf-8", "utf-16", "utf-32"]:
    for error in ["strict", "ignore", "replace",
                  "xmlcharrefreplace", "backslashreplace",
                  "add_one_codepoint", "add_utf16_bytes",
                  "add_utf32_bytes"]:

        try:
            print(encoding, error)
            b"\xff".decode(encoding, error)
            b"\xff\xff".decode(encoding, error)
            b"\xff\xff\xff".decode(encoding, error)
            b"\xff\xff\xff\xff".decode(encoding, error)
        except UnicodeDecodeError as e:
            print(e)
