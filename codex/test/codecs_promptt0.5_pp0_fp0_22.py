import codecs
# Test codecs.register_error

import codecs

class MyError(ValueError):
    pass

def my_error_handler(error):
    return u'', error.end

codecs.register_error('myerror', my_error_handler)

def check(encoding, input, output, error):
    # Encoding
    try:
        u = unicode(input, encoding, 'myerror')
    except MyError:
        u = u''
