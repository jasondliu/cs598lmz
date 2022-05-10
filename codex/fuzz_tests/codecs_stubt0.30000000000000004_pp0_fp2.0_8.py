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
    # UTF-8
    for encoding in ("utf-8", "utf_8"):
        for input, expected in [
            (b'\x80', "a"),
            (b'\x80\x80', "aa"),
            (b'\x80\x80\x80', "aaa"),
            (b'\x80\x80\x80\x80', "aaaa"),
            (b'\x80\x80\x80\x80\x80', "aaaaa"),
            (b'\x80\x80\x80\x80\x80\x80', "aaaaaa"),
            (b'\x80\x80\x80\x80\x80\x80\x80', "aaaaaaa"),
            (b'\x80\x80\x80\x80\x80\x80\x80\x80', "aaaaaaaa"),
            (b'\x80\x80\x80\x80\x80\x80\x80\x80\x80', "
