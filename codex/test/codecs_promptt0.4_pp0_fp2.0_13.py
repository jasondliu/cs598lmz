import codecs
# Test codecs.register_error

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u"\ufffd", exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def my_ignore(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u"", exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def my_strict(exc):
    if isinstance(exc, UnicodeDecodeError):
        raise TypeError("strict error handler")
    else:
        raise TypeError("don't know how to handle %r" % exc)

def my_xmlcharrefreplace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u"&#%d;" % ord(exc.object[exc.start]), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

