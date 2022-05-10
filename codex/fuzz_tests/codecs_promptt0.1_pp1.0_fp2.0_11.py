import codecs
# Test codecs.register_error

# This test is not exhaustive.  It only tests the error handling
# mechanism, not the actual codecs.

import codecs
import sys

def test_register_error():
    # Test registering an error handler
    def ignore_exception(exception):
        return (u'', exception.end)
    codecs.register_error('test.ignore', ignore_exception)
    # Test that the error handler is used
    s = u'\xff'
    u = s.encode('ascii', 'test.ignore')
    if u != u'':
        raise RuntimeError, 'encoding with test.ignore failed'
    # Test that the error handler is used for the right category
    s = u'\xff'
    u = s.encode('ascii', 'strict')
    if u != u'\xff':
        raise RuntimeError, 'encoding with strict failed'
    # Test that the error handler is used for the right encoding
    s = u'\xff'
    u = s.encode('latin-1', 'test.ignore
