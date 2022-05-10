import codecs
# Test codecs.register_error

import codecs

def hex_ignore_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [("%02x" % ord(c)) for c in exc.object[exc.start:exc.end]]
        return (u"\\x" + u"\\x".join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def hex_replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [("%02x" % ord(c)) for c in exc.object[exc.start:exc.end]]
        return (u"[" + u"][".join(s) + u"]", exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

