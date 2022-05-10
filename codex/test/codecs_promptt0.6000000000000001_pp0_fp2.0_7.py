import codecs
# Test codecs.register_error

def handle_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'\ufffd', exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.start + 1)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.strict", handle_error)

def test_encode(encoding):
    s = u"abc\u1234\u5678\u9abcdefg"
    for i in range(len(s)+1):
        for j in range(i, len(s)+1):
            u = s[i:j]
