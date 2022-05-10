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

def test(utf8, utf16, utf32, utf8b, utf16b, utf32b, ok):
    if not (utf8.decode("utf-8") == utf16.decode("utf-16-le") == utf32.decode("utf-32-le") ==
        utf8b.decode("utf-8-sig") == utf16b.decode("utf-16-be") == utf32b.decode("utf-32-be") == ok):
        print("Decode       ", utf8, utf16, utf32, utf8b, utf16b, utf32b)
        print("Decoded value", utf8.decode("utf-8"), utf16.decode("utf-16-le"), utf32.decode("utf-32-le"), utf8b.decode("utf-8-sig"), utf16b.decode("utf-16-be"), utf32b.decode("utf-32-be"))
        print("Ex
