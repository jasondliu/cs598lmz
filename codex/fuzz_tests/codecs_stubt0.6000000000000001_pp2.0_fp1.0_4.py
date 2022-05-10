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

def test_utf16_errors(encoding):
    def test():
        u = "\udcff"
        b = u.encode(encoding)
        uu = b.decode(encoding, "add_one_codepoint")
        assert len(u) + 1 == len(uu)
        assert u == uu[:-1]
        assert "\udcff" == uu[-1]
    test()
    for errors in ["ignore", "replace", "surrogateescape", "surrogatepass"]:
        try:
            test(errors)
        except UnicodeDecodeError:
            pass

def test_utf16_surrogatepass():
    u = "\udcff"
    b = u.encode('utf-16')
    assert b == b'\xff\xdc'
    uu = b.decode('utf-16', "surrogatepass")
    assert len(u) == len(uu)
    assert u == uu
    uu = b.decode('utf-16', "surrogate
