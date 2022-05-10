import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(encoding):
    print '-'*50
    print 'Encoding', encoding
    print '-'*50
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        print 'UCS2:', repr(u)
        print 'INPUT:', repr(u.encode(encoding, 'test.bad_encode'))
        print 'UNICODE:', repr(u.encode(encoding, 'test.bad_encode').decode(encoding, 'test.bad_decode'))
    except UnicodeError, detail:
        print '
