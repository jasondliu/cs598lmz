import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print '-'*20, encoding
    print 'encode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'test.my_error_handler'))
    print 'decode:', repr(u'\u3042\u3044\u3046\u3048\u304a'.encode(encoding, 'test.my_error_handler').decode(encoding, 'test.my_error_handler'))

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be']:
    test(encoding)
