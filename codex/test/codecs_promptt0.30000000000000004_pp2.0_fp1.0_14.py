import codecs
# Test codecs.register_error

# This test is for the case where the error handler is registered for a
# specific encoding.

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

# Now try to use it

