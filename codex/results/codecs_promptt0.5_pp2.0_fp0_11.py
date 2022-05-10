import codecs
# Test codecs.register_error
def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (exc.object[exc.start:exc.end], exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace", my_replace)

# Test codecs.lookup_error

def my_ignore(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u"", exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_ignore", my_ignore)

def my_strict(exc):
    if isinstance(exc, UnicodeDecodeError):
        raise UnicodeDecodeError("my_strict",
                                 exc.object,
                                 exc.start,
                                 exc.end,
                                 exc.reason)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codec
