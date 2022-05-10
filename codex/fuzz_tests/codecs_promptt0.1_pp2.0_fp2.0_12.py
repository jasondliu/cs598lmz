import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error', my_error_handler)

def test(encoding):
    print '-'*20, encoding, '-'*20
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'my_error'))
    print 'decode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'my_error').decode(encoding, 'my_error'))

for encoding in ['iso2022_jp', 'shift_jis', 'euc_jp', 'utf-8']:
    test(encoding)
