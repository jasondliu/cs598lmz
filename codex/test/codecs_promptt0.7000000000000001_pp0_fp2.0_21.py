import codecs
# Test codecs.register_error()

def handler(err):
    return (u"", err.start + 1)

codecs.register_error("test", handler)

