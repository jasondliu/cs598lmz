import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encode"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

for encoding in ('utf-8', 'iso-8859-1', 'ascii'):
    try:
        u = unicode('\xff', encoding, 'test.bad_decode')
    except UnicodeError, detail:
        print 'UnicodeError:', detail
    else:
        print 'no exception'
    try:
        s = u.encode(encoding, 'test.bad_encode')
    except UnicodeError, detail:
        print 'UnicodeError:', detail
    else:
        print 'no exception'
