import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(name, input, errors='strict'):
    print '%s: %r' % (name, input)
    try:
        print '%s: %r' % (name, input.decode(errors='test.bad_decode'))
    except UnicodeError, e:
        print 'UnicodeError:', e
    try:
        print '%s: %r' % (name, input.encode(errors='test.bad_encode'))
    except UnicodeError, e:
        print 'UnicodeError:', e

test('ascii', 'abc')
test('latin-1', '
