import codecs
# Test codecs.register_error

def ignore_errors(exc):
    if isinstance(exc, UnicodeDecodeError):
        return ('', exc.end)
    raise TypeError("don't know how to handle %r" % exc)

def xmlcharrefreplace_errors(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'&#%d;' % ord(exc.object[exc.start]), exc.end)
    raise TypeError("don't know how to handle %r" % exc)

def strict_errors(exc):
    raise exc

def strict_xmlcharrefreplace_errors(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'&#%d;' % ord(exc.object[exc.start]), exc.end)
    raise exc

def strict_ignore_errors(exc):
    if isinstance(exc, UnicodeDecodeError):
        return ('', exc.end)
    raise exc

def backslashreplace_errors(exc):
    if isinstance(exc, UnicodeEncodeError):
        return
