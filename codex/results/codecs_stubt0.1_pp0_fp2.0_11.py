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
    # test utf-16
    for encoding in ("utf-16", "utf-16-le", "utf-16-be"):
        for errors in ("strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes"):
            for input, expected in (
                ("\u3042", "\u3042"),
                ("\u3042\u3044", "\u3042\u3044"),
                ("\u3042\u3044\u3046", "\u3042\u3044\u3046"),
                ("\u3042\u3044\u3046\u3048", "\u3042\u3044\u3046\u3048"),
                ("\u3042\u3044\u3046\u3048\u304a", "\u3042\u3044\u3046\u3048\u304a"),
                ("\u3042\u3044\u3046\u3048\u304a\u304b
