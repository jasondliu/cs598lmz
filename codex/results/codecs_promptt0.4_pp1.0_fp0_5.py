import codecs
# Test codecs.register_error()

import codecs
import encodings

def force_replace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def force_ignore(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def force_xmlcharrefreplace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def force_backslashreplace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        return (u'', exc.end)
    else:
