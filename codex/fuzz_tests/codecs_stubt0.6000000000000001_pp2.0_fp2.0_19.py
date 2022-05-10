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

def test_utf8(name, value, errors='strict', expected=None):
    if expected is None:
        expected = value
    #
    for i in range(0, len(value)+1):
        for j in range(i, len(value)+1):
            s = value[i:j]
            #
            u = s.decode("utf-8", errors)
            assert u == expected
            #
            s2 = u.encode("utf-8", errors)
            assert s2 == value
            #
            if errors == 'strict':
                try:
                    u = s.decode("utf-8", 'add_one_codepoint')
                except UnicodeDecodeError:
                    pass
                else:
                    assert 0, '%s: %r should have raised UnicodeDecodeError' % \
                          (name, value)
                try:
                    s2 = u.encode("utf-8", 'add_one_codepoint')
                except UnicodeEncodeError:
                    pass
                else:
                    assert 0,
