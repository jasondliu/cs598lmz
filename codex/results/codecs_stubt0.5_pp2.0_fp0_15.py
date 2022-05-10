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
    for enc in ["utf-16", "utf-16-be", "utf-16-le"]:
        for inp, out in [("\u20ac", "€"), ("\ud800", "\ud800"),
                         ("\udc00", "\udc00"), ("\ud800\udc00", "\U00010000"),
                         ("\udbff\udfff", "\U0010ffff"),
                         ("\ud800\udc00\ud800\udc00", "\U00010000\U00010000"),
                         ("\ud800\udc00\ud800\udc00\ud800\udc00",
                          "\U00010000\U00010000\U00010000"),
                         ("\ud800\udc00\ud800\udc00\ud800\udc00\ud800\udc00",
                          "\U00010000\U00010000\U00010000\U00010000"),
                         ("\ud800\udc00\ud800\udc00\ud800\udc00\ud
