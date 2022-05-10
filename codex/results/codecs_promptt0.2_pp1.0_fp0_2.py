import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

def bad_encode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

def test(encoding):
    print '-'*50
    print 'Encoding', encoding
    try:
        u = u'\u3042'
        print 'UCS2:', repr(u.encode(encoding))
    except UnicodeError, err:
        print 'UCS2:', err
    try:
        u = u'\u3042\u3044'
        print 'UCS4:', repr(u.encode(encoding))
    except UnicodeError, err:
        print 'UCS4:', err
    try:
        print 'Decoding:', repr(u'\xff'.decode(encoding))
    except UnicodeError, err:

