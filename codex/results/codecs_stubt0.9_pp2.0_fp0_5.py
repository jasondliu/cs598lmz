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

def f(encoding):
    print("-*- encoding:", encoding)
    try:
        codecs.decode(b"\xff", encoding)
    except ValueError as e:
        print(e)
        print("repr(e):", repr(e))
    print("repr(e):", repr(e))
    try:
        codecs.decode(b"\x00\xff", encoding)
    except ValueError as e:
        print(e)
        print("repr(e):", repr(e))
    print("repr(e):", repr(e))
    try:
        codecs.decode(b"\x00\x00\xff", encoding)
    except ValueError as e:
        print(e)
        print("repr(e):", repr(e))
    print("repr(e):", repr(e))
    try:
        codecs.decode(b"\xff", encoding, errors="replace")
    except ValueError as e:
        print(e)
        print("repr
