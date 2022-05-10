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
    print name, ':',
    try:
        print codecs.decode(input, errors)
    except UnicodeError, err:
        print err

test('strict', '\xff')
test('replace', '\xff', 'replace')
test('ignore', '\xff', 'ignore')
test('xmlcharrefreplace', '\xff', 'xmlcharrefreplace')
test('test.bad_decode', '\xff', 'test.bad_decode')

test('strict', u'\u1234')
test('replace', u'\u1234', 'replace
