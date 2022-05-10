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

def check_one_codepoint(exc):
    if len(exc.object) != 1:
        raise TypeError("don't know how to handle %d codepoints"%len(exc.object))
    return (ord(exc.object) + 1,)

def check_utf16_bytes(exc):
    return tuple(map(ord, exc.object))

def check_utf32_bytes(exc):
    return tuple(map(ord, exc.object))

codecs.register_error("check_one_codepoint", check_one_codepoint)
codecs.register_error("check_utf16_bytes", check_utf16_bytes)
codecs.register_error("check_utf32_bytes", check_utf32_bytes)

def test_main():
    # encoding
    s = u"a\u1234"
    for codec in ["ascii", "utf-8", "utf-16", "utf-16-be"]:
        for errors in ["strict", "replace", "xmlcharrefreplace",
