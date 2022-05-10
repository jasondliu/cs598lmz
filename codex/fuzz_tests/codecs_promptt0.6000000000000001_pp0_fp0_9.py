import codecs
# Test codecs.register_error(name, error_handler)
# Test codecs.lookup_error(name).

# The encoding is registered with the name "test"
# The errors are reported as UnicodeDecodeErrors
# The error handler is called with a UnicodeDecodeError object.
# The handler returns a tuple (unicode object, length consumed)
# The handler is expected to be called twice.

# This handler is designed to return the correct Unicode string
# for the "test" encoding.

class TestError(Exception):
    pass

def handler(error):
    print("handler called")
    if error.start != error.end:
        raise TestError("wrong start/end")
    if not isinstance(error.object, bytes):
        raise TestError("object is not a bytes object")
    if error.end > len(error.object):
        raise TestError("end > len(object)")
    return (chr(error.object[error.end]) * 2, 1)

codecs.register_error("test", handler)

if codecs.lookup_error("test") is
