import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.lookup', handler)

def test(encoding):
    print encoding
    print '-' * 30
    for s in [u'abc', u'\u20ac', u'\u20ac\u20ac', u'\u20ac\u20ac\u20ac']:
        print repr(s), '->',
        try:
            print repr(s.encode(encoding, 'test.lookup'))
        except UnicodeEncodeError, e:
            print 'UnicodeEncodeError:', e
        print
    print

test('ascii')
test('latin-1')
test('iso8859-15')
test('utf-8')
test('utf-16')
test('utf-16-le')
test('utf-16-be')
test('utf-32')
test('utf-32-le')
test('utf-
