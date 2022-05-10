import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'Got', exception.__class__.__name__
    return u'', exception.end

codecs.register_error('test', handler)

print 'TEST 1'
print '-' * 20

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding', encoding
    print '-' * 20
    print codecs.decode('\xff', encoding, 'test')
    print codecs.decode('\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff\xff\
