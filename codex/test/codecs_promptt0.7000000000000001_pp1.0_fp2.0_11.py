import codecs
# Test codecs.register_error()
# First, get a utf-8 encoding with xmlcharrefreplace error
def xmlcharreplace(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u''.join(u'&#%d;' % ord(c) for c in exc.object[exc.start:exc.end]),
            exc.end)
codecs.register_error("test.xmlcharrefreplace", xmlcharreplace)
