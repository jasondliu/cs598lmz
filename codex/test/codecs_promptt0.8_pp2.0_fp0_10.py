import codecs
# Test codecs.register_error().
import codecs

def strict_ignore(exc):
    return (u'', exc.end)

def strict_replace(exc):
    return (u'\ufffd', exc.end)

def strict_escape(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u"\\u%04x" % ord(exc.object[exc.start]), exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        return (u"\\u%04x" % exc.object[exc.start:exc.start + 2], exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def strict_surrogateescape(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (chr(exc.object[exc.start]), exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        return (exc.object[exc.start], exc.end)
