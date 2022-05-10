import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(name, input, errors='strict'):
    print '%s: %r' % (name, input)
    print ' ', codecs.decode(input, 'ascii', errors)
    print ' ', codecs.encode(input, 'ascii', errors)

test('strict', 'abc\xff')
test('ignore', 'abc\xff', 'ignore')
test('replace', 'abc\xff', 'replace')
test('xmlcharrefreplace', 'abc\xff', 'xmlcharrefreplace')
test('test.bad_decode', 'abc\xff', 'test.bad_decode')
test('test.bad_encode', 'abc\xff
