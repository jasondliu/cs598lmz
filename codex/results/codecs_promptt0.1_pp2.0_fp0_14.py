import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print '-', encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.my_error_handler')
        print repr(s)
    except UnicodeError, e:
        print 'UnicodeError:', e

for encoding in ['iso8859-1', 'ascii', 'utf-7', 'utf-8']:
    test(encoding)
