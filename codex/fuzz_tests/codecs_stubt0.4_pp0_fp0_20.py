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
    # Test encoding
    for enc in ["utf-8", "utf-16", "utf-32"]:
        for err in ["strict", "replace", "ignore", "add_one_codepoint",
                    "add_utf16_bytes", "add_utf32_bytes"]:
            for s in [b"abc", b"\xf0\x90\x80\x80", b"\xf4\x90\x80\x80"]:
                try:
                    codecs.encode(s, enc, err)
                except UnicodeEncodeError:
                    pass
                else:
                    raise AssertionError("%s/%s should have raised UnicodeEncodeError" % (enc, err))

    # Test decoding
    for enc in ["utf-8", "utf-16", "utf-32"]:
        for err in ["strict", "replace", "ignore", "add_one_codepoint",
                    "add_utf16_bytes", "add_utf32_bytes"]:
            for s in [b"abc
