import codecs
# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    elif isinstance(exc, UnicodeEncodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('my_replace', my_replace)

