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

def test(encoding):
    print(encoding, "->", encoding.upper(), ":", end=' ')
    try:
        print(codecs.decode(b'\xff', encoding, "add_one_codepoint"), end=' ')
        print(codecs.decode(b'\xff\xff', encoding, "add_utf16_bytes"), end=' ')
        print(codecs.decode(b'\xff\xff\xff\xff', encoding, "add_utf32_bytes"), end=' ')
    except UnicodeDecodeError as exc:
        print(exc)

for encoding in ["utf-8", "utf-16", "utf-32", "ascii"]:
    test(encoding)
