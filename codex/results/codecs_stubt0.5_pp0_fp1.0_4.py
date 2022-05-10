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
    # Testing UTF-16 encoding
    for encoding in ("utf-16-be", "utf-16-le"):
        for input, expected in (
            ("\xe4\xbd\xa0\xe5\xa5\xbd", "\xe4\xbd\xa0\xe5\xa5\xbd"),
            ("\xe4\xbd\xa0\xe5\xa5\xbd", "\xbd\xa0\xe5\xa5\xbd"),
            ("\xe4\xbd\xa0\xe5\xa5\xbd", "\xa0\xe5\xa5\xbd"),
            ("\xe4\xbd\xa0\xe5\xa5\xbd", "\xe5\xa5\xbd"),
            ("\xe4\xbd\xa0\xe5\xa5\xbd", "\xa5\xbd"),
            ("\xe4\xbd\xa0\xe5\xa5\xbd", "\xbd"),
            ("\xe4\xbd\xa
