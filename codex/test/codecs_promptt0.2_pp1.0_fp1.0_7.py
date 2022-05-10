import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test the 'ignore' error handler
