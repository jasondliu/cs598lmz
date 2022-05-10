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

def test(name, codec, value, errors=None):
    print((name, value))
    if errors is None:
        errors = "strict"
    s = codec.encode(value, errors=errors)
    print(repr(s))
    st = str(s, "unicode-escape")
    print('"'+st+'"')
    v = codec.decode(s, errors=errors)
    if v != value:
        print((value, v))

test("ascii", "ascii", "Hello")
test("ascii", "ascii", "Hello\u1234")
test("ascii", "ascii", "Hello\u1234", "replace")
test("ascii", "ascii", "Hello\u1234", "ignore")
test("ascii", "ascii", "Hello\u1234", "xmlcharrefreplace")

test("latin-1", "latin-1", "Hello\u1234")
test("latin-1", "latin-1
