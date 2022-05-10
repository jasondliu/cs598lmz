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
    for name in ("utf-8", "utf-16", "utf-32"):
        for errors in ("ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            for byteorder in (-1, 0, 1):
                for byteorder2 in (-1, 0, 1):
                    print("testing decoding", name, errors, byteorder, byteorder2)
                    decode_and_encode(name, errors, byteorder, byteorder2)

def decode_and_encode(name, errors, byteorder, byteorder2):
    if name == "utf-16" and byteorder2 == 0:
        byteorder2 = -1
    if name == "utf-32" and byteorder2 == 0:
        byteorder2 = -1
    if byteorder == 0:
        byteorder = -1
    if byteorder2 == 0:
        byteorder2 = -1
    if byteorder == -1:
        byteorder = sys.byteorder
    if byte
