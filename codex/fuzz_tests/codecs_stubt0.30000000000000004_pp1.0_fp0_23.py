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

# test surrogatepass

def test_surrogatepass(encoding):
    u = '\ud800\udc00'
    b = u.encode(encoding)
    u2 = b.decode(encoding)
    assert u2 == u

def test_surrogatepass_error(encoding):
    u = '\ud800\udc00'
    b = u.encode(encoding)
    b = b[:-1]
    u2 = b.decode(encoding, "surrogatepass")
    assert u2 == u

def test_surrogatepass_error2(encoding):
    u = '\ud800\udc00'
    b = u.encode(encoding)
    b = b[:-1]
    try:
        u2 = b.decode(encoding)
    except UnicodeDecodeError:
        pass
    else:
        raise Exception("should have raised")

def test_surrogatepass_error3(encoding):
    u = '\ud800\
