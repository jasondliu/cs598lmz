import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.lookup', handler)

