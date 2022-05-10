import codecs
# Test codecs.register_error
#
# This test is for issue #5166: when the codecs.register_error() function is
# called with a 'name' argument, the error handler is not registered.
#
# The test is simple: we register an error handler for the 'ignore' codec,
# and then we try to encode a string using this codec. If the error handler
# is not registered, the test will fail.

def test_error_handler(exc):
    return (u'', exc.end)

codecs.register_error('test.ignore', test_error_handler)
codecs.encode('abc', 'ignore', 'test.ignore')
