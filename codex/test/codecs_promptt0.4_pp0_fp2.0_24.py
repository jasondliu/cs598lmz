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
