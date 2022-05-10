import codecs
# Test codecs.register_error() and codecs.lookup_error()

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    elif isinstance(exc, UnicodeEncodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.replace", replace_error)

def strict_error(exc):
    raise exc

codecs.register_error("test.strict", strict_error)

def ignore_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    elif isinstance(exc, UnicodeEncodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.ignore", ignore_error)

