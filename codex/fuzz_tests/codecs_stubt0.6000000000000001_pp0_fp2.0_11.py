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
    print("=" * 60)
    print(encoding, "errors='strict'")
    s = b'\xff\xfe\xff\xff'
    try:
        u = s.decode(encoding)
    except UnicodeDecodeError as exc:
        print(exc)

    print(encoding, "errors='add_one_codepoint'")
    s = b'\xff\xfe\xff\xff'
    try:
        u = s.decode(encoding, "add_one_codepoint")
    except UnicodeDecodeError as exc:
        print(exc)

    print(encoding, "errors='add_utf16_bytes'")
    s = b'\xff\xfe\xff\xff'
    try:
        u = s.decode(encoding, "add_utf16_bytes")
    except UnicodeDecodeError as exc:
        print(exc)

    print(encoding, "errors='add_utf32_bytes'")
    s = b'\xff\
