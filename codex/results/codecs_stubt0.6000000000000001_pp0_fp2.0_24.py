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

def test_main():
    # Encoding
    u = "a\uDC80b"
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            try:
                encoded = u.encode(encoding, errors)
            except Exception as exc:
                print("Exception:", repr(exc))
            else:
                print("Encoded:", repr(encoded))
    # Decoding
    for u in ["a\uDC80b", "a\uD800b", "a\uD800\uDC80b"]:
        for encoding in ("utf-8", "utf-16", "utf-32"):
            for errors in ("strict", "replace", "ignore",
                           "add_one_codepoint", "add_utf16_bytes",
                           "add_utf32_bytes"):
                try:
                    dec
