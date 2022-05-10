import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

print '%r' % u'\u3042\u3044'.encode('euc-jp', 'test.lookup'),
print '%r' % u'\u3042\u3044'.encode('euc-jp', 'test.lookup'),
print '%r' % u'\u3042\u3044'.encode('euc-jp', 'test.lookup'),
print '%r' % u'\u3042\u3044'.encode('euc-jp', 'test.lookup'),
print '%r' % u'\u3042\u3044'.encode('euc-jp', 'test.lookup'),
print '%r' % u'\u3042\u3044'.encode('euc-jp', 'test.lookup'),
print '%r' % u'\u
