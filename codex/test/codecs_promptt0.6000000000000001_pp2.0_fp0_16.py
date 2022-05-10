import codecs
# Test codecs.register_error
def my_replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = exc.object[exc.start:exc.end]
        return s.replace("\r", "?"), exc.end
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("myreplace", my_replace_error)

