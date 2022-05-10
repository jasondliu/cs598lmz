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
    # test unicode-internal-unicode
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for u in ("\u3042", "\u3042\u3042", "\u3042\u3042\u3042"):
                u2 = u.encode(encoding, errors).decode(encoding, errors)
                if u != u2:
                    print("Failed:", encoding, errors, u, u2)

if __name__ == "__main__":
    test_main()
