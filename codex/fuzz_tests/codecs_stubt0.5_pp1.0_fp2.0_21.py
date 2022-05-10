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

import ctypes

def test(name, enc, dec, errors):
    print("testing %s" % name)
    s = "abc\u1234\u5678"
    b = s.encode(enc)
    s2 = b.decode(dec, errors=errors)
    if s != s2:
        print("error: %s != %s" % (s, s2))

test("utf-8/utf-8", "utf-8", "utf-8", "strict")
test("utf-8/utf-8", "utf-8", "utf-8", "replace")
test("utf-8/utf-8", "utf-8", "utf-8", "backslashreplace")
test("utf-8/utf-8", "utf-8", "utf-8", "ignore")
test("utf-8/utf-8", "utf-8", "utf-8", "xmlcharrefreplace")
test("utf-8/utf-8", "utf-8", "utf-8", "add_one_codepoint
