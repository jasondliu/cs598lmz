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

# Test encoding
for encoding in ("utf-8", "utf-16", "utf-32"):
    for error_handler in ("strict", "ignore", "replace", "add_one_codepoint",
                          "add_utf16_bytes", "add_utf32_bytes"):
        for unistr in (u"\u1234", u"\U00012345"):
            try:
                bytes = unistr.encode(encoding, error_handler)
            except UnicodeEncodeError:
                pass
            else:
                print(repr(bytes), encoding, error_handler)

# Test decoding
for encoding in ("utf-8", "utf-16", "utf-32"):
    for error_handler in ("strict", "ignore", "replace", "add_one_codepoint",
                          "add_utf16_bytes", "add_utf32_bytes"):
        for bytes in (b"\xe1\x88\xb4", b"\xf0\x92\x8d\x85"):
           
