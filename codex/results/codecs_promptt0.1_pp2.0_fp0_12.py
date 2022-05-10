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
    try:
        u = u'\u3042\u3044\u3046\u3048\u304a'
        s = u.encode(encoding, 'test.bad_encode')
    except UnicodeError, detail:
        print 'Encode:', detail
    try:
        s = '\x82\xa0\x82\xa2\x82\xa4\x82\xa6\x82\xa8'
        u = s.decode(encoding, 'test.bad_decode')
    except Unicode
