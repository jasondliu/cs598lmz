import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print '-'*20, encoding
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'my_error')
        print repr(s)
    except UnicodeEncodeError, e:
        print e

for encoding in ['iso-2022-jp', 'shift_jis', 'euc_jp', 'utf-8']:
    test(encoding)
