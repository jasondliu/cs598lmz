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

def test_utf_16(name, errors, exc, res_unicode, res_bytes):
    assert (name + ".encode(errors=%s)" % errors)
    try:
        unicode(name+"\udc00\u0041", "utf-16", errors)
    except UnicodeEncodeError as e:
        assert e.reason == exc
    else:
        assert False, "Didn't raise"
    assert (name + ".decode(errors=%s)" % errors)
    try:
        unicode(name+"\udc00\u0041", "utf-16", errors)
    except UnicodeEncodeError as e:
        assert e.reason == exc
    else:
        assert False, "Didn't raise"
    assert (name + ".encode(errors=%s)" % errors)
    try:
        unicode(name+"\udc00\u0041", "utf-16", errors)
    except UnicodeEncodeError as e:
        assert e.reason == exc
    else:
        assert False,
