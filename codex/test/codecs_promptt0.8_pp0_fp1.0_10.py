import codecs
# Test codecs.register_error()

def handler(exc):
    if issubclass(exc, UnicodeEncodeError):
        return (u'REPLACEMENT CHARACTER', exc.end)
    if issubclass(exc, UnicodeDecodeError):
        return (u'REPLACEMENT CHARACTER', exc.start + 1)
    raise TypeError("don't know how to handle %r" % exc)

