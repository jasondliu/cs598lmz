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

