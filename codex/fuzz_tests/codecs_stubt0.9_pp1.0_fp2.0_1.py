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

def raise_utf8_decode_exception(exc):
    # Cython uses a different UTF8 decoding routine from the CPython standard
    # library that produces a different unicode string at the end. To get the
    # same exception, we use a string of different bytes
    return (b'\xed\xbf\xbf\xed\xa0\xbf', exc.start)

codecs.register_error("raise_utf8_decode_exception", raise_utf8_decode_exception)

if __name__ == "__main__":
    # Test [int].translate()
    r = [0, 1, 2]
    r[2] = 4
    r.translate(None, None)
    t = r.translate({1: 2})
    t[0] = 3
    # Test str
    s = "    abc\xFF"
    print(s)
    print(s)
    print(s.index("a"))
    print(s.index("x"))
    print(s.index(
