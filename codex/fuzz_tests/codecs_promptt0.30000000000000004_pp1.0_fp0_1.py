import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad', bad_decode)
codecs.register_error('test.bad', bad_encode)

def test(input, errors='strict'):
    try:
        print '%r.decode(%r) =>' % (input, errors),
        print repr(input.decode('ascii', errors))
    except UnicodeError, exc:
        print 'UnicodeError:', exc
    try:
        print '%r.encode(%r) =>' % (input, errors),
        print repr(input.encode('ascii', errors))
    except UnicodeError, exc:
        print 'UnicodeError:', exc

test('abc')
test('\xff')
test(u'abc')
test(u'\xff')

print 'Trying bad_decode...
