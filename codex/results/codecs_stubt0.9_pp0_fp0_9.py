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

def test(str, codec, table):
    print ">>>", str, codec, table
    print eval(str).encode(codec, table)

test('"a\u1234"', "ascii", None)
test('"a\u1234"', "ascii", "add_one_codepoint")
test('"a\u1234"', "ascii", "add_utf16_bytes")
test('"a\u1234"', "ascii", "add_utf32_bytes")
test('"a\u1234"', "utf-16", None)
test('"a\u1234"', "utf-16", "add_one_codepoint")
test('"a\u1234"', "utf-16", "add_utf16_bytes")
test('"a\u1234"', "utf-16", "add_utf32_bytes")
test('"a\u1234"', "utf-32", None)
test('"a\u1234"', "utf-32", "
