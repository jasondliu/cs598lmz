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
    if u != output:
        raise ValueError, "encoding failed"

    # Decoding
    try:
        s = unicode(output, 'latin-1', 'myerror').encode(encoding)
    except MyError:
        s = ''
    if s != input:
        raise ValueError, "decoding failed"

check('myerror', 'abc', u'abc', None)
check('myerror', 'abc\xff', u'abc', None)
check('myerror', 'abc\xff', u'abc', MyError)
