import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\u1111'.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, e:
        print 'ERROR:', e
    else:
        print 'OK'

test('ascii')
test('latin-1')
test('iso-8859-1')
test('iso-8859-15')
test('iso-8859-2')
test('iso-8859-3')
test('iso-8859-4')
test('iso-8859-5')
test('iso-8859-6')
test('iso-8859-7')
test('iso-8859-8')
test('iso-8859-9')
test('iso-8859-10')
test('iso-8859-13')
