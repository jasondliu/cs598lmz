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
    # Test with a unicode-to-unicode mapping
    for encoding in ("utf-16", "utf-32"):
        for error_handler in ("ignore", "replace", "xmlcharrefreplace",
                              "backslashreplace", "namereplace"):
            try:
                u = "\uFFFC".encode(encoding, error_handler)
            except UnicodeEncodeError:
                pass
            else:
                raise TestFailed("UnicodeEncodeError should have been raised")

    # Test with a unicode-to-bytes mapping
    for encoding in ("utf-16-be", "utf-16-le", "utf-32-be", "utf-32-le"):
        for error_handler in ("ignore", "replace", "xmlcharrefreplace",
                              "backslashreplace", "namereplace"):
            try:
                u = "\uFFFC".encode(encoding, error_handler)
            except UnicodeEncodeError:
                pass
            else:
                raise TestFailed("UnicodeEn
