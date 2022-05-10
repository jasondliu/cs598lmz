import codecs
# Test codecs.register_error

import codecs

def raise_exc(exc):
    raise exc

def replace_exc(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'', exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    elif isinstance(exc, UnicodeTranslateError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def ignore_exc(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError,
                        UnicodeTranslateError)):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def xmlcharrefreplace_exc(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'&#%d;' % ord(exc.object[exc.start]), exc.end)
