import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(name, input, errors):
    print '%s: %r, %s' % (name, input, errors)
    try:
        print '  ', codecs.charmap_encode(input, errors)
    except UnicodeError, e:
        print '  ', e
    try:
        print '  ', codecs.charmap_decode(input, errors)
    except UnicodeError, e:
        print '  ', e

test('strict', u'\u3042', 'strict')
test('replace', u'\u3042', 'replace')
test('ignore', u'\u3042',
