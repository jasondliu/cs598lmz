import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called for', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print 'Trying', encoding
    try:
        u'\ud800'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'Got exception:', err
        print 'reason:', err.reason
        print 'object:', err.object
        print 'start:', err.start
        print 'end:', err.end
        print 'encoding:', err.encoding
        print 'end:', err.end

test('ascii')
test('latin-1')
test('test.lookup')
