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
    print '%r, %s' % (input, errors)
    print '  ', repr(input.decode(errors=errors))
    print '  ', repr(input.encode(errors=errors))

test('abc')
test('\xff')
test('\xff', 'ignore')
test('\xff', 'replace')
test('\xff', 'xmlcharrefreplace')
test('\xff', 'backslashreplace')
test('\xff', 'namereplace')
test('\xff', 'test.bad_decode')
test('\xff', 'test.bad_encode')

# Test codecs.lookup

