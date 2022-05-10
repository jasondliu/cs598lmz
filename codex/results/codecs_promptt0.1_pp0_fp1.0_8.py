import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print '\nEncoding:', encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.myerror')
    except UnicodeEncodeError, e:
        print 'ERROR:', e

# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error_handler)

for encoding in ['ascii', 'latin-1', 'utf-8'
