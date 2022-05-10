import codecs
# Test codecs.register_error()

# This test doesn't actually test the error handler, but it does test
# that we can register an error handler.

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Create a codec that uses the error handler.
codecs.register(lambda name: (None, None, None, None))

# Test that the codec can be used.
