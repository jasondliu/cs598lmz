import codecs
# Test codecs.register_error()

# Test the 'xmlcharrefreplace' error handler

def xmlcharrefreplace_handler(exc):
    if isinstance(exc, UnicodeEncodeError):
        s = [u'&#%d;' % ord(exc.object[idx]) for idx in xrange(exc.start, exc.end)]
        return (u''.join(s), exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        s = [unichr(int(exc.object[idx:idx+2])) for idx in xrange(exc.start, exc.end, 2)]
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.xmlcharrefreplace', xmlcharrefreplace_handler)

def test_xmlcharrefreplace(encoding):
    # Encode
    u = u'\u3042\u3044\u3046'
