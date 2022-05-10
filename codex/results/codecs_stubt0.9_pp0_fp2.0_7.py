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

def test(func, name, input, expected):
    actual = func(input)
    if actual != expected:
        print(name + ":", repr(input), "->", repr(expected), "- expected; but got", repr(actual))

# Test utf_8_decode
# Tests found in Modules/test_codecs.py in the stdlib
test(codecs.getdecoder('utf-8'), "utf-8", b'\xc2\x80\xed\xa0\x80', ('\u0080' + u'\ud800', 2))
test(codecs.getdecoder('utf-8'), "utf-8", b'\xed\xa0\x80\xed\xbf\xbf', (u'\ud800' + u'\udfff', 4))
test(codecs.getdecoder('utf-8'), "utf-8", b'\xc2\x80\xed\xa0', ('\u0080' + u'\ud800', 2))
test(codecs.
