import codecs
# Test codecs.register_error

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [u'\ufffd'] * len(exc.object[exc.start:exc.end])
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace", my_replace)

# test UnicodeDecodeError
s = '\x81\x82\x83\x84'
