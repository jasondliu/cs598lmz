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

def _test(encoding):
    s = "".join("-%s-" % unichr(i) for i in range(10000, 11000, 2))  # NOTE: py3k compatible

    try:
        b = s.encode(encoding)
    except UnicodeEncodeError, exc:
        x1 = str(exc)
        if encoding in ["utf_16", "utf_16_be", "utf_16_le"]:
            b1 = b.decode(encoding, "add_utf16_bytes").encode(encoding)
        elif encoding in ["utf_32", "utf_32_be", "utf_32_le"]:
            b1 = b.decode(encoding, "add_utf32_bytes").encode(encoding)
        else:
            b1 = b.decode(encoding, "add_one_codepoint").encode(encoding)
        try:
            u1 = b1.decode(encoding)
        except UnicodeDecodeError, exc:
            x2 = str(
