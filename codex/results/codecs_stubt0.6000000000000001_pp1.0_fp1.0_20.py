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

def check(encoding, input, add_bytes, expected):
    actual = input.decode(encoding, "add_%s_bytes" % add_bytes)
    assert actual == expected, '%r != %r' % (actual, expected)
    actual = input.decode(encoding, "replace")
    assert actual == expected.replace(u'\ufffd', u'?'), '%r != %r' % (actual, expected)
    actual = input.decode(encoding, "ignore")
    assert actual == expected.replace(u'\ufffd', u''), '%r != %r' % (actual, expected)

def test_ascii():
    check('ascii', b'abc', 'one', 'abc')
    check('ascii', b'abc', 'utf16', 'abc')
    check('ascii', b'abc', 'utf32', 'abc')
    check('ascii', b'\xff', 'one', '\ufffd')
    check('ascii', b'\xff', 'utf
