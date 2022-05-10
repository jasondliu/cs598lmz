import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.myerrorhandler', my_error_handler)

def test(encoding):
    print 'TEST', encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.myerrorhandler')
        print 'S', repr(s)
    except UnicodeError, e:
        print 'ERROR', e

for encoding in ('euc_jp', 'iso2022_jp', 'shift_jis', 'utf_8'):
    test(encoding)
