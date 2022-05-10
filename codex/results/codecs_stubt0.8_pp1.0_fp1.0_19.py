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
    fail_encodings(add_one_codepoint, b'abcd',
            "utf-8", "ascii", "utf-7", "utf-16-be", "utf-16-le", "utf-32-be",
            "utf-32-le", "raw_unicode_escape", "unicode_escape", "unicode_internal",
            "mbcs", "oem"
        )
    fail_decodings(add_utf16_bytes, "abcd",
            "utf-32-le", "utf-32-be"
        )
    fail_decodings(add_utf32_bytes, "abcd",
            "utf-16-le", "utf-16-be"
        )

if __name__ == "__main__":
    test_main()
