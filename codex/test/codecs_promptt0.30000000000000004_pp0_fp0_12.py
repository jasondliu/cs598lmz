import codecs
# Test codecs.register_error

def handler(exception):
    return ('', exception.end)

codecs.register_error('test.ignore', handler)

