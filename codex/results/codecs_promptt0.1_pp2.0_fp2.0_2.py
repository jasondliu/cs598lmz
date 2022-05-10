import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print 'my_error:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error)

def test(encoding):
    print 'TEST:', encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.myerror')
    except UnicodeError, e:
        print 'ERROR:', e

for encoding in ['iso8859-1', 'ascii', 'utf-7', 'utf-8']:
    test(encoding)

print 'DONE'
