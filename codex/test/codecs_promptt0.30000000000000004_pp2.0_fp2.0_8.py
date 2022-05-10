import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

utf8_decoder = codecs.getincrementaldecoder('utf-8')()
