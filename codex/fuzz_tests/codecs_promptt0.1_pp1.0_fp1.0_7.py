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
    try:
        result = input.decode(name, errors)
    except UnicodeError, e:
        result = str(e)
    if result != expected:
        print "Error: %s.decode(%s, %s) = %s, expected %s" % (
            repr(input), repr(name), repr(errors), repr(result), repr(expected))

test('ascii', 'abc', 'test.bad_decode', 'bad decode')
test('ascii', 'abc', 'test.bad_encode', 'abc')
test('ascii', '
