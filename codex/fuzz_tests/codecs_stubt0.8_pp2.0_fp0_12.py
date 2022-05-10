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

# Test round trip failure for ASCII
s1 = "abc\xFF\xFF"
for encoding in ("ascii", "utf-8", "utf-16", "utf-32"):
    for bad_handler in ("strict", "add_one_codepoint", "add_utf16_bytes",
                        "add_utf32_bytes"):
        try:
            result = s1.encode(encoding, bad_handler)
            print("result1 =", repr(result))
            result.decode(encoding, bad_handler)
            print("result2 =", repr(result))
        except UnicodeError as exc:
            print("Caught", exc.__class__.__name__, "encoding", encoding,
                  "handler", bad_handler, "position", exc.start)

# Test round trip failure for Unicode
s2 = "abc\uD800\uE000"
for encoding in ("ascii", "utf-8", "utf-16", "utf-32"):
    for bad_handler in ("strict", "replace",
