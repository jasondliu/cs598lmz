import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.my_handler', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print '  u"abc".encode(%r)' % encoding
    print '  ', u"abc".encode(encoding, 'test.my_handler')
    print '  u"\u1234".encode(%r)' % encoding
    print '  ', u"\u1234".encode(encoding, 'test.my_handler')
    print '  u"\u1234".encode(%r, "ignore")' % encoding
    print '  ', u"\u1234".encode(encoding, 'ignore')
    print '  u"\u1234".encode(%r, "replace")' % encoding
    print '  ', u"\u1234".encode(
