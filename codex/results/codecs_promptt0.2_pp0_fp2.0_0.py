import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print 'handler called:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print 'Trying', encoding
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
        print 'retval', repr(e.object), 'end', e.end
    print

test('ascii')
test('latin-1')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('unicode-escape')
test('raw-unicode-escape')
test('unicode-internal')
test('test.lookup')
