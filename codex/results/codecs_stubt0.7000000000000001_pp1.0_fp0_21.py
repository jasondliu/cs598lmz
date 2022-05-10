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
    for suffix in ("", "_error"):
        f = codecs.getincrementalencoder(encoding + suffix)()
        f.encode(b'a', "replace")
        f.encode(b'b', "replace")
        res = f.encode(b'c', "replace")
        f.reset()
        f.encode(b'a', "replace")
        f.encode(b'b', "replace")
        res2 = f.encode(b'c', "replace")
        if res != res2:
            print("%s: %r != %r" % (encoding, res, res2))
        f.encode(b'\xff', "replace")
        res = f.encode(b'a', "replace")
        f.reset()
        f.encode(b'\xff', "replace")
        res2 = f.encode(b'a', "replace")
        if res != res2:
            print("%s: %r != %r" %
