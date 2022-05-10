import codecs
# Test codecs.register_error

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        x = u''.join(unichr(0xfffd) for c in exc.object[exc.start:exc.end])
        return (x, exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.replace", my_replace)

