import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\ud800'.encode(encoding, 'test.lookup')
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e
    else:
        print 'no exception'

test('ascii')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-32-be')
test('latin-1')
test('iso-8859-1')
test('iso-8859-15')
test('cp1252')
test('cp437')
test('cp850')
test('cp852')
test('cp866')
test('koi8_r
