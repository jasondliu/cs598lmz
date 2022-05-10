import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
    print '-'*20, encoding
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'test.ignore'))
    print 'decode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'test.ignore').decode(encoding, 'test.ignore'))

for encoding in ['iso2022_jp', 'shift_jis', 'euc_jp', 'utf_8']:
    test(encoding)

# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

def test(encoding):
