import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.myerror', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print '%10s  %r' % (encoding, u'\u20ac'.encode(encoding, 'test.myerror'))

print '%10s  %r' % ('replace', u'\u20ac'.encode('ascii', 'replace'))
print '%10s  %r' % ('ignore', u'\u20ac'.encode('ascii', 'ignore'))
print '%10s  %r' % ('xmlcharrefreplace', u'\u20ac'.encode('ascii', 'xmlcharrefreplace'))
