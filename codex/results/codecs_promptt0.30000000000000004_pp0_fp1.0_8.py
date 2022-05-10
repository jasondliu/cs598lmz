import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test', handler)

def test(encoding):
    print encoding
    try:
        u'\ufffe'.encode(encoding)
    except UnicodeEncodeError, e:
        print '  ', e
        print '  ', repr(e.object)
        print '  ', e.start
        print '  ', e.end
        print '  ', e.reason
        print '  ', e.encoding
        print '  ', e.object[e.start:e.end]
        print '  ', e.object[e.start:e.end].encode(e.encoding)
        print '  ', e.object[e.start:e.end].encode(e.encoding, 'test')

for encoding in ['utf-8', 'iso8859-1', 'ascii', 'latin-1']:
    test(encoding)

# Test codecs.register_error()
