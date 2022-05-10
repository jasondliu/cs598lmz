import codecs
# Test codecs.register_error

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

# replace
codecs.register_error("test.replace", my_replace)

