import codecs
# Test codecs.register_error("test.xmlcharrefreplace", xmlcharrefreplace)

def xmlcharrefreplace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [u'&#%d;' % ord(c) for c in exc.object[exc.start:exc.end]]
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def xmlcharrefreplace_errors(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [u'&#%d;' % ord(c) for c in exc.object[exc.start:exc.end]]
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

