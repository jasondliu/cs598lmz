import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Exception:', exception
    return (u'', exception.end)

codecs.register_error('test.myerror', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print 'Encoded  :', codecs.encode('abc\xff', encoding, 'test.myerror')
    print 'Decoded  :', codecs.decode('abc\xff', encoding, 'test.myerror')
    print
