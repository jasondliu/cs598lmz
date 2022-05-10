import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', handler)

def test(encoding):
    print '-'*20, encoding
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'ERROR:', err

test('ascii')
test('latin-1')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('test.lookup')
