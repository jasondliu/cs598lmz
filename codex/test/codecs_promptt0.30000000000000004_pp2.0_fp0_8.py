import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('test.ignore', handler)

