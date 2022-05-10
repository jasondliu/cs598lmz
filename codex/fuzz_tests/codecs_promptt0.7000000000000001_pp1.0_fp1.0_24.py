import codecs
# Test codecs.register_error:
def xmlcharrefreplace_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        s = [ u'&#%d;' % ord(c) for c in exc.object[exc.start:exc.end] ]
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)
codecs.register_error('test.xmlcharrefreplace', xmlcharrefreplace_error)
def test_codecs_1():

    import codecs

    s = u"\u3042\u3044\u3046\u3048\u304a"
    for encoding in [ "utf-7", "utf-8", "utf-16", "utf-32", "unicode-internal" ]:
        x = codecs.encode(s, encoding)
        y = codecs.decode(x, encoding)
        if s != y: raise TestFailed, "%s failed" % encoding

    for encoding in [ "ascii", "latin-
