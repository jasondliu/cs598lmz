import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print 'my_error_handler called'
    return (u'', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

def test(encoding):
    print 'TEST', encoding
    try:
        u'\udc00'.encode(encoding, 'test.my_error_handler')
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    print

for encoding in ['ascii', 'latin-1', 'utf-8']:
    test(encoding)
