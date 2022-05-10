import codecs
# Test codecs.register_error()

def handler(exception):
    return ("**", exception.end)

codecs.register_error("test.ignore", handler)

# This should raise an error even with the error handler
# (because "replace" will not be called since ignore=True)
