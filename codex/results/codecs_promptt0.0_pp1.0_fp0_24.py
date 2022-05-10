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
    print '%s: %r (%s)' % (name, input, errors)
    try:
        print ' ', codecs.decode(input, 'ascii', errors)
    except UnicodeError, e:
        print '  ', e
    try:
        print ' ', codecs.encode(input, 'ascii', errors)
    except UnicodeError, e:
        print '  ', e

test('strict', 'abc\xff')
test('replace', 'abc\xff', 'replace')
test('ignore', 'abc\xff', 'ignore')
test('xml
