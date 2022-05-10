import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def ignore_exc(exc):
    pass

def xmlcharrefreplace_exc(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    l = []
    for c in exc.object[exc.start:exc.end]:
        l.append("&#%d;" % ord(c))
    return ("".join(l), exc.end)

def backslashreplace_exc(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    l = []
    for c in exc.object[exc.start:exc.end]:
        l.append('\\x%02x' % ord(c))
    return ("".join(l), exc.end)

