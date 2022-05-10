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
    # Test UTF-16 and UTF-32 codecs
    for encoding in ("utf-16", "utf-32"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            # Encode
            s = "abc"
            if encoding == "utf-16":
                expected = b'\xff\xfea\x00b\x00c\x00'
            else:
                expected = b'\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00'
            if errors == "replace":
                expected = expected[:2] + b'?' * 10 + expected[-2:]
            elif errors == "ignore":
                expected = expected[:2] + expected[-2:]
            elif errors == "add_one_codepoint":
                expected = expected[:2] +
