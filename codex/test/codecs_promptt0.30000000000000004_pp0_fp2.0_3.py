import codecs
# Test codecs.register_error

# This test was added to check that the codecs module handles
# the case where the error handler is not callable

def my_error_handler(exception):
    return (u"", exception.end)

codecs.register_error("test.notcallable", my_error_handler)

# The codecs module should raise a TypeError when the error handler
# is not callable
try:
    codecs.register_error("test.notcallable", "not callable")
except TypeError:
    pass
