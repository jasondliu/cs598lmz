import codecs
# Test codecs.register_error

import codecs

def raise_exception(exc):
    raise exc

def ignore_exception(exc):
    pass

def replace_exception(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def xmlcharrefreplace_exception(exc):
    if isinstance(exc, UnicodeEncodeError):
        s = [u'&#%d;' % ord(exc.object[exc.start])]
        for c in exc.object[exc.start+1:exc.end]:
            s.append(u'&#%d;' % ord(c))
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def backslashreplace_exception(exc):
    if isinstance(exc, UnicodeEncodeError):
        s = [u'\\x%02x' % ord(
