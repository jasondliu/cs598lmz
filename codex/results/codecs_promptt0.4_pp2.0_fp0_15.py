import codecs
# Test codecs.register_error

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace", my_replace)

def my_ignore(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_ignore", my_ignore)

def my_xmlcharrefreplace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'&#%d;' % ord(exc.object[exc.start]), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_xmlcharrefreplace", my_xmlcharrefreplace)

def
