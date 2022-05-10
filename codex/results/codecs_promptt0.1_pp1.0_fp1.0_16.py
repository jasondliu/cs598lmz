import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test that the error handler is used
assert codecs.decode('abc\x80def', 'ascii', 'test.ignore') == u'abcdef'

# Test that the error handler is used for the surrogateescape error handler
assert codecs.decode('abc\x80def', 'ascii', 'surrogateescape') == u'abc\udc80def'

# Test that the error handler is used for the surrogatepass error handler
assert codecs.decode('abc\x80def', 'ascii', 'surrogatepass') == u'abc\udc80def'

# Test that the error handler is used for the ignore error handler
assert codecs.decode('abc\x80def', 'ascii', 'ignore') == u'abcdef'

# Test that the error handler is used for the replace error handler
assert codecs.decode('abc\x80def', '
