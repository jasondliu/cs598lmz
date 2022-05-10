import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler called with %r' % exception
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print 'Encoding:', encoding.encode('ascii')
    print 'Encoding:', encoding.encode('ascii', 'test.ignore')
    print 'Encoding:', encoding.encode('ascii', 'test.ignore')
    print 'Encoding:', encoding.encode('ascii', 'test.ignore')
    print 'Encoding:', encoding.encode('ascii', 'test.ignore')
    print 'Encoding:', encoding.encode('ascii', 'test.ignore')
    print 'Encoding:', encoding.encode('ascii', 'test.ignore')
    print 'Encoding:', encoding.encode('ascii', 'test.ignore')
    print 'Enc
