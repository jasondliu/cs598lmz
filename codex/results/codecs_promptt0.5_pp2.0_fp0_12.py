import codecs
# Test codecs.register_error()

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = str(exc)
        return (u'!', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def xmlcharrefreplace_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        s = str(exc)
        return (u'!', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def ignore_error(exc):
    if isinstance(exc, (UnicodeDecodeError, UnicodeEncodeError)):
        s = str(exc)
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def strict_error(exc):
    if isinstance(exc, (UnicodeDecodeError, UnicodeEncodeError)):
        s = str(exc)
        raise UnicodeError(s)
    else:
