import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(name, input, errors, expected):
    print name, errors,
    try:
        result = input.decode(errors=errors)
    except UnicodeError, detail:
        print 'UnicodeError:', detail
        if str(detail) != expected:
            print '*** expected', expected
    else:
        print repr(result)
        if result != expected:
            print '*** expected', repr(expected)

test('strict', '\xff', 'strict', 'bad decode')
test('strict', '\xff', 'test.bad_decode', 'bad decode')
test('strict', '\xff', '
