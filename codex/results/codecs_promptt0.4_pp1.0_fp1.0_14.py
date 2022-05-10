import codecs
# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace", my_replace)

print codecs.decode("abc\xff\xfe\xffdef", "utf-8", "my_replace")
print codecs.decode("abc\xff\xfe\xffdef", "utf-16", "my_replace")
print codecs.decode("abc\xff\xfe\xffdef", "ascii", "my_replace")

# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace",
