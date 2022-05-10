import codecs
# Test codecs.register_error by registering an error handler that uses
# XML-style references.
def xmlcharrefreplace_errors(exc):
    if isinstance(exc, UnicodeEncodeError):
        s = [u'&#%d;' % ord(c) for c in exc.object[exc.start:exc.end]]
        return (u''.join(s), exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        s = [unichr(int(c[2:-1])) for c in exc.object[exc.start:exc.end].split(u'&#')
             if c.endswith(u';')]
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)
codecs.register_error("test.xmlcharrefreplace", xmlcharrefreplace_errors)

