import codecs
# Test codecs.register_error()

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print '-'*20, encoding
    try:
        u'\u1111'.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, err:
        print 'ERROR:', err

test('ascii')
test('latin-1')
test('iso-8859-1')
test('iso-8859-2')
test('iso-8859-15')
test('koi8-r')
test('cp1252')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('unicode-internal')
