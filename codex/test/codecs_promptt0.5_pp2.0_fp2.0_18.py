import codecs
# Test codecs.register_error()

import codecs, string, sys

def handler(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u"?", exc.start + 1)
    raise TypeError("don't know how to handle %r" % exc)

