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
