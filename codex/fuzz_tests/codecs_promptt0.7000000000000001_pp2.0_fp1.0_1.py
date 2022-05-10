import codecs
# Test codecs.register_error:
#   - register an error handler that sends all replacement
#     characters to uppercase
class my_error(codecs.LookupError):
    pass

def my_handler(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    res = []
    for c in exc.object[exc.start:exc.end]:
        if isinstance(c, str):
            c = ord(c)
        res.append(unichr(c).upper())
    return (u"".join(res), exc.end)

def my_handler_with_exc(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    res = []
    for c in exc.object[exc.start:exc.end]:
        if isinstance(c, str):
            c = ord(c)
        res.append(unichr(c).upper())
    return (u"".join
