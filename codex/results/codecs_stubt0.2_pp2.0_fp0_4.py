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
    # Test UTF-16
    for enc in ("utf-16", "utf-16-le", "utf-16-be"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes"):
            for s in ("abc", "a\udc80b", "a\udc80\udc80b", "a\udc80\udc80\udc80b"):
                if errors == "add_utf16_bytes":
                    # The error handler is called twice, so we expect the
                    # string to be doubled.
                    expected = s + s
                else:
                    expected = s
                assert codecs.decode(codecs.encode(s, enc, errors), enc, errors) == expected

    # Test UTF-32
    for enc in ("utf-32", "utf-32-le", "utf-32-be"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint", "add_
