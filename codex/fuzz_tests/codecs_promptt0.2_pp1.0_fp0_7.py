import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print '-'*20, encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.my_error_handler')
        print repr(s), type(s)
    except UnicodeError, e:
        print e

for encoding in ['iso8859-1', 'iso8859-15', 'ascii', 'utf-8']:
    test(encoding)
