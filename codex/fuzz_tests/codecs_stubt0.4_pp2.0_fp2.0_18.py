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
    # test for issue #4
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for error_handler in ("strict", "add_one_codepoint",
                              "add_utf16_bytes", "add_utf32_bytes"):
            print(encoding, error_handler)
            try:
                codecs.decode(b'\xf0\x90\x80', encoding, error_handler)
            except UnicodeDecodeError as e:
                print(e)

if __name__ == "__main__":
    test_main()
