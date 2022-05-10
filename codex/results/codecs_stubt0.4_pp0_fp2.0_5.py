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
    # test for bug #1098990
    for encoding in ("utf-7", "utf-8", "utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            print(encoding, errors)
            try:
                u = "\x81".encode(encoding, errors)
            except UnicodeError:
                pass
            else:
                print(repr(u))
                if errors == "add_one_codepoint":
                    assert u == b"a"
                elif errors == "add_utf16_bytes":
                    assert u == b"ab"
                elif errors == "add_utf32_bytes":
                    assert u == b"abcd"

if __name__ == "__main__":
    test_main()
