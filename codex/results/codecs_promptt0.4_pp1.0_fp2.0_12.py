import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

for encoding in ['utf-8', 'utf-16', 'iso-8859-1']:
    print '%s:' % encoding
    print codecs.decode('\xff', encoding, 'test.lookup')
    print codecs.decode('\xff\xff', encoding, 'test.lookup')
    print codecs.decode('\xff\xff\xff', encoding, 'test.lookup')
    print codecs.decode('\xff\xff\xff\xff', encoding, 'test.lookup')
    print codecs.decode('\xff\xff\xff\xff\xff', encoding, 'test.lookup')
    print codecs.decode('\xff\xff\xff\xff\xff\xff', encoding, 'test.lookup')
    print codecs.decode('\xff\xff\xff\xff\xff\xff\xff', encoding,
