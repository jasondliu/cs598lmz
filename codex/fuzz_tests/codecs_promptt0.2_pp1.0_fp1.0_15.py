import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called'
    return (u'', exception.end)

codecs.register_error('test.myerror', handler)

def test(encoding):
    print 'TEST', encoding
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'UnicodeEncodeError:', err
        print 'reason:', err.reason
        print 'object:', err.object
        print 'start:', err.start
        print 'end:', err.end
    print

for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16'):
    test(encoding)

test('test.myerror')
