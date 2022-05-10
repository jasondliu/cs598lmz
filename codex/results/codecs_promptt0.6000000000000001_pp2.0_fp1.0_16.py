import codecs
# Test codecs.register_error()

# We don't actually use the file, but we need a filename
f = tempfile.TemporaryFile()

def replace_error(exc):
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u'', exc.end)

def ignore_error(exc):
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u'', exc.end)

def xmlcharref_error(exc):
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u'&#%d;' % ord(exc.object[exc.start:exc.end]), exc.end)

def backslashreplace_error(exc):
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u'
