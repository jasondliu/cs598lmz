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
    print '%r, %s ->' % (input, errors),
    try:
        print repr(input.decode(errors=errors))
    except UnicodeError, err:
        print 'ERROR:', err

test('\xff')
test('\xff', 'ignore')
test('\xff', 'replace')
test('\xff', 'xmlcharrefreplace')
test('\xff', 'backslashreplace')
test('\xff', 'test.bad_decode')

test(u'\u1234')
test(u'\u1234', 'ignore')
test(u'\u1234', 'replace')

