import codecs
# Test codecs.register_error
def g1(exc):
    if isinstance(exc, UnicodeEncodeError):
        x, = exc.args
        return (u'&#%d;' % ord(x), 1)
    elif isinstance(exc, UnicodeDecodeError):
        x, = exc.args
        return (unichr(int(x[2:-1])), 1)
