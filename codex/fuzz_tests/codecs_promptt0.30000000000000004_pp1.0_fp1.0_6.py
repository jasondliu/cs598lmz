import codecs
# Test codecs.register_error()

def handler(exception):
    print 'Handling %s' % exception.__class__.__name__
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print codecs.decode('\xff', encoding, 'test.strict')
    print codecs.decode('\xff', encoding, 'strict')
    print codecs.decode('\xff', encoding, 'ignore')
    print codecs.decode('\xff', encoding, 'replace')
    print codecs.decode('\xff', encoding, 'xmlcharrefreplace')
    print codecs.decode('\xff', encoding, 'backslashreplace')
    print codecs.decode('\xff', encoding, 'namereplace')
    print codecs.decode('\xff', encoding, 'surrogateescape')
    print codecs.decode('\xff', encoding, 'surrogate
