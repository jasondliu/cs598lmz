import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(name, input, errors):
    print '%s: %s' % (name, errors)
    try:
        print repr(input.decode(name, errors))
    except UnicodeError, err:
        print 'UnicodeError:', err
    try:
        print repr(input.encode(name, errors))
    except UnicodeError, err:
        print 'UnicodeError:', err

test('ascii', 'abc', 'strict')
test('ascii', 'abc', 'ignore')
test('ascii', 'abc', 'replace')
test('ascii', 'abc', 'xmlcharrefreplace')
test('ascii',
