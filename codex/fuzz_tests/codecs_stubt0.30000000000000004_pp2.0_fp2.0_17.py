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
    # Test that the utf-16 and utf-32 codecs can handle surrogates correctly
    # in the error handlers.
    for encoding in ("utf-16", "utf-32"):
        for error_handler in ("add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            try:
                codecs.decode("\xed\xa0\x80", encoding, error_handler)
            except UnicodeDecodeError:
                pass
            else:
                raise AssertionError("UnicodeDecodeError not raised")

if __name__ == "__main__":
    test_main()
