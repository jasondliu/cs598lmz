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

def check_error_handler(encoding):
    try:
        b"\x80".decode(encoding)
        raise Exception("should have thrown")
    except UnicodeDecodeError as e:
        print(e)
        print(e.object)
        print(e.start)
        print(e.end)
        print(e.reason)
        print(e.object[e.start:e.end])
    print()
    print(b"\x80".decode(encoding, "strict"))
    print(b"\x80".decode(encoding, "replace"))
    print(b"\x80".decode(encoding, "ignore"))
    print(b"\x80".decode(encoding, "add_one_codepoint"))
    print(b"\x80\x80".decode(encoding, "add_utf16_bytes"))
    print(b"\x80\x80\x80\x80".decode(encoding, "add_utf32_bytes"))
    print()

