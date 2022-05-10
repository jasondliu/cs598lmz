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
    print(repr(codecs.decode(b'\xc3', encoding, 'add_one_codepoint')))
    print(repr(codecs.decode(b'\x61', encoding, 'add_one_codepoint')))
    print(repr(codecs.decode(b'\xc3', encoding, 'add_utf16_bytes')))
    print(repr(codecs.decode(b'\x61', encoding, 'add_utf16_bytes')))
    print(repr(codecs.decode(b'\xc3', encoding, 'add_utf32_bytes')))
    print(repr(codecs.decode(b'\x61', encoding, 'add_utf32_bytes')))

for encoding in ["utf-8", "utf-8-sig"]:
    print(encoding)
    test(encoding)
