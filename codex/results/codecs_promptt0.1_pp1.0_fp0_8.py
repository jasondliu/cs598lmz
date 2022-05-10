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
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, exception:
        print 'UnicodeEncodeError:', exception
    else:
        print 'no exception'

test('ascii')
test('latin-1')
test('utf-8')
test('test.lookup')

# Test codecs.lookup_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding, ':',
    try:
        u'\udc00'.encode(encoding)
    except UnicodeEncodeError, exception:
        print
