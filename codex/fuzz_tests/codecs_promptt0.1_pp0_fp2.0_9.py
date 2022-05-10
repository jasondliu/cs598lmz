import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
        print 'start:', e.start
        print 'end:', e.end
        print 'object:', repr(e.object)
        print 'reason:', e.reason
        print 'encoding:', e.encoding
        print 'end:', e.end
        print 'args:', e.args
    print

test('ascii')
test('latin-1')
test('utf-8')
test('test.lookup')
