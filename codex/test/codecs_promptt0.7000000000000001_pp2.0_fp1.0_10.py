import codecs
# Test codecs.register_error().

def handler(exception):
    return ("code: %d" % exception.start, exception.end)

codecs.register_error("test.myencodeerrorhandler", handler)
codecs.register_error("test.mydecodeerrorhandler", handler)

