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
        # Test decoding
        for error in ("strict", "replace", "ignore", "add_one_codepoint",
                      "add_utf16_bytes", "add_utf32_bytes"):
            for byteorder in (-1, 0, 1):
                if byteorder == 0:
                    byteorder = sys.byteorder
                if encoding == "utf-16" and error == "add_utf32_bytes":
                    continue
                if encoding == "utf-32" and error == "add_utf16_bytes":
                    continue
                if encoding == "utf-16" and error == "add_one_codepoint":
                    continue
                if encoding == "utf-32" and error == "add_one_codepoint":
                    continue
                if encoding == "utf-16" and error == "ignore":
                    continue
                if encoding == "utf-32" and error == "ignore":
                    continue
                if encoding ==
