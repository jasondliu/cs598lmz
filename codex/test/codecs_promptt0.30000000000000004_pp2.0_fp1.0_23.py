import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error', my_error_handler)

encoding = 'ascii'
text = u'\u00e0\u00e1\u00e2'

