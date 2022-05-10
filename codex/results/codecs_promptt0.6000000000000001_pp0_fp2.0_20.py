import codecs
# Test codecs.register_error()

import codecs

def f(exc):
    if isinstance(exc, UnicodeEncodeError):
        res = u"".join([u"\\u%04x" % ord(c) for c in u"\uFFFD"] * len(exc.object[exc.start:exc.end]))
    elif isinstance(exc, UnicodeDecodeError):
        res = u"".join([u"\\u%04x" % ord(c) for c in u"\uFFFD"] * len(exc.object[exc.start:exc.end]))
    else:
        raise TypeError("don't know how to handle %r" % exc)
    return (res, exc.end)

codecs.register_error("test", f)

def test(encoding):
    print encoding
    print '-'*60
    print "Encode:",
    s = u"abc\u3042\u3044\u3046\u3048\u304a"
    for errors in "strict", "replace", "ignore", "test":
