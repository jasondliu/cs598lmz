import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'ERROR:', err
    print

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    test(encoding)

print 'TEST SUCEEDED'
