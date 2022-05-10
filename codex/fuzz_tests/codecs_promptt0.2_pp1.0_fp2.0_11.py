import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my.error', my_error_handler)

def test(encoding):
    print '-'*20, encoding
    print u'\u3042'.encode(encoding, 'my.error'),
    print repr(u'\u3042'.encode(encoding, 'my.error'))
    print u'\u3042\u3044'.encode(encoding, 'my.error'),
    print repr(u'\u3042\u3044'.encode(encoding, 'my.error'))
    print u'\u3042\u3044\u3046'.encode(encoding, 'my.error'),
    print repr(u'\u3042\u3044\u3046'.encode(encoding, 'my.error'))

for encoding in ['iso2022_jp', 'shift_jis', 'euc_jp', 'utf-8']:

