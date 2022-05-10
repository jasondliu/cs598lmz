import codecs
# Test codecs.register_error

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.start + 1)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def my_ignore(exc):
    return (u'', exc.start + 1)

def my_xmlcharrefreplace(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    s = []
    for c in exc.object[exc.start:exc.end]:
        s.append(u'&#%d;' % ord(c))
    return (u''.join(s), exc.end)

def my_backslashreplace(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    s = []
