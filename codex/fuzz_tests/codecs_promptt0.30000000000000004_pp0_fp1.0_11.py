import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception

codecs.register_error('test', handler)

def test(encoding):
    print encoding, ':',
    try:
        codecs.lookup_error('test')(u'\u1111')
    except UnicodeError, e:
        print e

test('ascii')
test('latin-1')
test('utf-8')
test('utf-16')
test('utf-32')
