import codecs
# Test codecs.register_error()

def strict_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('UnicodeDecodeError:', exc.object, exc.start, exc.end, exc.reason)
        y = exc.object[exc.start:exc.end]
        print('Y:', y, type(y))
        x = '?'*len(y)
        print('X:', x, type(x))
        return (x, exc.end)
    elif isinstance(exc, UnicodeEncodeError):
        print('UnicodeEncodeError:', exc.object, exc.start, exc.end, exc.reason)
        y = exc.object[exc.start:exc.end]
        print('Y:', y, type(y))
        x = '?'*len(y)
        print('X:', x, type(x))
        return (x, exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

