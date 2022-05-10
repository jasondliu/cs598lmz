import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('my_error', my_error_handler)

