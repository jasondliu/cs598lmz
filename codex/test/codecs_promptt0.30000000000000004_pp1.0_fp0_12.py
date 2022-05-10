import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.start + 1)

codecs.register_error('test', handler)

# Test that the handler is called
s = '\xff\xff\xff'
