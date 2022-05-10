import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    print 'encode'
    print '-'*20
    for i in range(256):
        c = chr(i)
        try:
            s = c.encode(encoding, 'my_error')
        except UnicodeEncodeError, e:
            print i, repr(c), 'UnicodeEncodeError:', e.__class__.__name__
        else:
            print i, repr(c), repr(s)
    print '-'*20
    print 'decode'
    print '-'*20
    for i in range(256):
        c = chr(i)
        try:
            s = c.decode(encoding, 'my_error')
        except UnicodeDecodeError, e:
            print i, repr(c
