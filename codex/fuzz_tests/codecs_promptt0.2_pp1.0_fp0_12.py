import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', my_error_handler)

def test(encoding):
    print '-', encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.myerror')
        print 'encode:', repr(s)
    except UnicodeError, e:
        print 'ERROR:', e
    try:
        s = '\x82\xA0\x82\xA2\x82\xA4\x82\xA6\x82\xA8'
        u = s.decode(encoding, 'test.myerror')
        print 'decode:', repr(u)
    except UnicodeError, e:
        print 'ERROR:', e

for encoding in ['iso2022_
