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
    print 'input:', repr(input)
    print 'errors:', errors
    print 'decode:', repr(input.decode(errors=errors))
    print 'encode:', repr(input.encode(errors=errors))
    print

test('abc')
test('\xff')
test('abc', 'test.bad_decode')
test('\xff', 'test.bad_decode')
test('abc', 'test.bad_encode')
test('\xff', 'test.bad_encode')

# Test codecs.lookup

import codecs

def test(encoding):
    print '
