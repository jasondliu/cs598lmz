import codecs
# Test codecs.register_error

def handler(ex):
    return (u'@', ex.end)

codecs.register_error('test', handler)

# Lookup error handler by name
codecs.lookup_error('test')

# Lookup error handler by handler function
codecs.lookup_error(handler)

# Check that we can encode/decode with this error handler
decoded = u'\udc00\ud800'.encode('utf-8', 'test')
encoded = '\x00@\x80@'.decode('utf-8', 'test')

# Check that the error handler was called with the right exception
def handler2(ex):
    if not isinstance(ex, UnicodeEncodeError):
        raise TypeError("handler2 got %r" % ex)
    return (u'@', ex.end)

codecs.register_error('test2', handler2)
decoded = u'\udc00\ud800'.encode('utf-8', 'test2')

# Check that the error handler was called with the right
