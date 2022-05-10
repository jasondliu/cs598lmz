import codecs
# Test codecs.register_error()

# This test is not very complete, but it does at least check that
# the error handler is called.

import codecs
import sys

#
# This codec does not exist, so the error handler should be called
#

def test_register_error_1():
    # This should raise a LookupError
    try:
        codecs.lookup('test_register_error_1')
    except LookupError:
        pass
    else:
        raise TestFailed, 'codecs.lookup() should have raised a LookupError'
    # Now register an error handler
    def handler(exception):
        print 'handler called'
        return ('', exception.end)
    codecs.register_error('test.register_error_1', handler)
    # Now try to look up the codec again
    try:
        codecs.lookup('test_register_error_1')
    except LookupError:
        print 'handler not called'
    else:
        raise TestFailed, 'codecs.lookup() should have raised a LookupError
