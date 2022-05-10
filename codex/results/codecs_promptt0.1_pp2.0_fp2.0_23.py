import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    print 'encode:', repr(u'\u20ac\u20ac\u20ac'.encode(encoding, 'test.lookup'))
    print 'decode:', repr(u'\u20ac\u20ac\u20ac'.encode(encoding).decode(encoding, 'test.lookup'))

test('ascii')
test('latin-1')
test('utf-8')
test('utf-16')
test('utf-32')
test('unicode-internal')

# Test codecs.register_error() with a function

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

def test(encoding):
    print encoding
    print 'encode
