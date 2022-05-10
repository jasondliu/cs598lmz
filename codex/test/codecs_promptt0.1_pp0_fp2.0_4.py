import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test', handler)

# Test that the error handler is used
s = '\x80'
