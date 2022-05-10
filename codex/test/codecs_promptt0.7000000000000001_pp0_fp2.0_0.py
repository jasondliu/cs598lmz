import codecs
# Test codecs.register_error

def handler(ex):
    return (u'@', ex.end)

codecs.register_error('test', handler)

# Lookup error handler by name
codecs.lookup_error('test')

# Lookup error handler by handler function
