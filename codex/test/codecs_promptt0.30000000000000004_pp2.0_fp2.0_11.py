import codecs
# Test codecs.register_error()

import codecs

def replace_errors(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.replace", replace_errors)

