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
    # Test UTF-7 codec
    for encoding, errors in (("utf-7", "strict"),
                             ("utf-7", "replace"),
                             ("utf-7", "ignore"),
                             ("utf-7", "add_one_codepoint"),
                             ("utf-7", "add_utf16_bytes"),
                             ("utf-7", "add_utf32_bytes")):
        print("Encoding:", encoding, "Errors:", errors)
        print("Unicode -> UTF-7")
        for input, output in (
            ("abc", b"+ACE-"),
            ("\u20ac", b"+AOQ-"),
            ("\u20ac\u20ac", b"+AOQAOQ-"),
            ("\u20ac\u20ac\u20ac", b"+AOQAOQAOQ-"),
            ("\u20ac\u20ac\u20ac\u20ac", b"+AOQAOQAOQAO
