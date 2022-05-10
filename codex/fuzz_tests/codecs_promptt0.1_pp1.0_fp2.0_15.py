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
    print '%s: %r (%s) ->' % (name, input, errors),
    try:
        output = codecs.decode(input, name, errors)
    except UnicodeError, err:
        print 'ERROR:', err
    else:
        print '%r' % output

test('ascii', 'abc')
test('ascii', '\xff')
test('ascii', '\xff', 'ignore')
test('ascii', '\xff', 'replace')
test('ascii', '\xff', 'test.bad_decode')
