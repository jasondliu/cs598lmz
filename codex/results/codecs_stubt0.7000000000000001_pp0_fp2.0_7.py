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

def check_unicode_replace(input, errors="strict", expected=None):
    if expected is None:
        expected = input.decode(errors=errors)
    res = input.decode('ascii', errors=errors)
    print(repr(input), repr(errors), repr(res), repr(expected))
    assert res == expected

def test_unicode_replace():
    check_unicode_replace('abc\xff')
    check_unicode_replace(b'abc\xff')
    check_unicode_replace(b'abc\xff', errors='ignore')
    check_unicode_replace(b'abc\xff', errors='replace', expected='abc\ufffd')
    check_unicode_replace(b'abc\xff', errors='add_one_codepoint', expected='abca')
    check_unicode_replace(b'abc\xff', errors='add_utf16_bytes', expected='abca')
    check_unicode_replace(b'abc\xff', errors='add_utf32_bytes', expected='abca
