import codecs
# Test codecs.register_error()
import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test', handler)

for encoding in ['ascii', 'utf-8']:
    print 'Encoding:', encoding
    print codecs.decode('\xff', encoding, 'test')
    print codecs.decode('\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff\xff\xff\xff', encoding, 'test')
    print codecs.decode('\xff\xff\xff\xff\xff\xff\xff\xff', encoding, 'test')
