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

def test_main():
    # test utf-16-le
    for i in range(0x10000):
        c = chr(i)
        if i <= 0xffff:
            b = c.encode("utf-16-le")
        else:
            b = c.encode("utf-16-le", "surrogatepass")
        if i <= 0xffff:
            c2 = b.decode("utf-16-le")
        else:
            c2 = b.decode("utf-16-le", "surrogatepass")
        assert c == c2

    # test utf-16-be
    for i in range(0x10000):
        c = chr(i)
        if i <= 0xffff:
            b = c.encode("utf-16-be")
        else:
            b = c.encode("utf-16-be", "surrogatepass")
        if i <= 0xffff:
            c2 = b.decode("utf-16-be")
        else:
            c
