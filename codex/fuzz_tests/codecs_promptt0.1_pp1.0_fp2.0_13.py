import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(input, errors='strict'):
    try:
        print '%r.decode(%r, %r) =' % (input, errors, input.decode(errors=errors)),
        print repr(input.decode(errors=errors))
    except UnicodeError, exc:
        print 'UnicodeError:', exc
    try:
        print '%r.encode(%r, %r) =' % (input, errors, input.encode(errors=errors)),
        print repr(input.encode(errors=errors))
    except UnicodeError, exc:
        print 'UnicodeError:', exc

test(u'abc')
test(u
