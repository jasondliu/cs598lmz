import codecs
# Test codecs.register_error

import codecs

def raise_exception(exc):
    raise exc

def replace_with_x(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'x', exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        return (u'x', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def ignore_exception(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def xmlcharrefreplace_handler(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'&#%d;' % ord(exc.object[exc.start]), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

