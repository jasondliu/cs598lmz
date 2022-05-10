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

for codec in [ "ascii", "latin-1", "utf-8", "utf-16", "utf-32" ]:
    print("testing", codec, "...")
    # decode error
    try:
        b'2\xd8\x00'.decode(codec, "add_one_codepoint")
    except UnicodeDecodeError as exc:
        if exc.object != b'2\xd8\x00' or exc.start != 1 or exc.end != 3:
            raise
    else:
        raise RuntimeError("expected UnicodeDecodeError")
    # encode error
    try:
        '\U00022000'.encode(codec, "add_one_codepoint")
    except UnicodeEncodeError as exc:
        if exc.object != '\U00022000' or exc.start != 0 or exc.end != 1:
            raise
    else:
        raise RuntimeError("expected UnicodeEncodeError")
    # surrogate pass-through in decode
    text = b'\xd8\x00\xd8\x
