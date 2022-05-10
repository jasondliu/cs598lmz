import codecs
# Test codecs.register_error()

import codecs

def raise_exc(exc):
    raise exc

def ignore_exc(exc):
    return u'', exc.end

def xmlcharrefreplace_exc(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    l = []
    for c in exc.object[exc.start:exc.end]:
        l.append(u'&#%d;' % ord(c))
    return (u''.join(l), exc.end)

