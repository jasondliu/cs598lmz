import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error_handler', my_error_handler)

