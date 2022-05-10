import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Got', exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print codecs.decode('abc\xffdef', encoding, 'test')
    print codecs.decode(u'abc\uffffdef', encoding, 'test')
    print codecs.decode('abc\xffdef', encoding, 'ignore')
    print codecs.decode('abc\xffdef', encoding, 'replace')
    print codecs.decode(u'abc\uffffdef', encoding, 'ignore')
    print codecs.decode(u'abc\uffffdef', encoding, 'replace')
    print codecs.encode('abc\xffdef', encoding, 'test')
    print codecs.encode(u'abc\uffffdef', encoding, 'test')
    print codecs.
