import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\ud800'.encode(encoding)
    except UnicodeEncodeError, err:
        print 'UnicodeEncodeError:', err
    else:
        print 'no error'

test('ascii')
test('utf-8')
test('utf-16')
test('utf-16-be')
test('utf-16-le')
test('utf-16-ex')
test('utf-16-be-ex')
test('utf-16-le-ex')
test('utf-32')
test('utf-32-be')
test('utf-32-le')
test('utf-32-ex')
test('utf-32-be-ex')
test('utf-32-le-ex')
test('unicode-escape')
test('raw-unicode
