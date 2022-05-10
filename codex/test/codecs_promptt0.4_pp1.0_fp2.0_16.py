import codecs
# Test codecs.register_error
def bad_decode(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('DecodeError:', exc.reason, exc.object[exc.start:exc.end])
        return ('', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.bad_decode', bad_decode)

