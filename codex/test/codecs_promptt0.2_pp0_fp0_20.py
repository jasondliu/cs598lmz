import codecs
# Test codecs.register_error

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.strict", handler)

# Test that the error handler is called
