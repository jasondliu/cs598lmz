import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return '<ERROR>', exception.end

codecs.register_error('my_error', my_error_handler)

utf8 = codecs.lookup('utf-8')

